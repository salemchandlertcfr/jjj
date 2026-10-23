"""Invariantes locais da condutora; não substituem evals de agentes/ambientes.

Os dossiês e remotos usados aqui são temporários. Nenhum teste acessa o GitHub.
"""
from __future__ import annotations

import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / 'skills' / 'etapa-1-cir' / 'scripts'
sys.path.insert(0, str(SCRIPTS))


class CondutoraTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.core = importlib.import_module('_core')
        cls.registrar_module = importlib.import_module('registrar')
        cls.brief = importlib.import_module('brief')
        cls.vigia = importlib.import_module('vigia')
        cls.pendencias = importlib.import_module('pendencias')

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='cir-unittest-')
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / 'dossie'
        self.session = 'sessao-A'
        self.git_identity = mock.patch.dict(os.environ, {
            'GIT_AUTHOR_NAME': 'CIR Test',
            'GIT_AUTHOR_EMAIL': 'cir-test@example.invalid',
            'GIT_COMMITTER_NAME': 'CIR Test',
            'GIT_COMMITTER_EMAIL': 'cir-test@example.invalid',
            'GIT_CONFIG_NOSYSTEM': '1',
            'GIT_CONFIG_GLOBAL': os.devnull,
            'PYTHONDONTWRITEBYTECODE': '1',
        })
        self.git_identity.start()
        self.addCleanup(self.git_identity.stop)
        self.cli('dossie_init.py', self.root, '--projeto', 'Teste CIR',
                 '--session', self.session)
        self.cli('estado.py', 'dose', self.root, '--session', self.session,
                 '--planejada', 'padrao', '--usada', 'padrao',
                 '--motivo', 'Dose do cenário de teste')

    def cli(self, script, *args, success=True):
        result = subprocess.run(
            [sys.executable, '-B', str(SCRIPTS / script), *map(str, args)],
            capture_output=True, text=True, timeout=20,
        )
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def git(self, *args):
        result = subprocess.run(
            ['git', '-C', str(self.root), *map(str, args)],
            capture_output=True, text=True, timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def state(self):
        return self.core.load_state(self.root)

    def update_state(self, **changes):
        state = self.state()
        state.update(changes)
        self.core.save_state(self.root, state)
        return self.state()

    def snapshot(self):
        return {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in self.root.rglob('*')
            if path.is_file() and '.git' not in path.relative_to(self.root).parts
            and path.name not in {'.trava'}
        }

    def complete_steps(self, through):
        for number in range(1, through + 1):
            args = ['passo', self.root, '--session', self.session,
                    '--numero', number, '--evidencia', f'Evidência do passo {number}']
            if number == 2:
                args.extend(['--origem', 'usuario'])
            self.cli('estado.py', *args)

    def checkpoint(self, **changes):
        payload = {
            'tipo': 'checkpoint', 'contexto': 'Entendimento inicial confirmado.',
            'escolha': 'Manter o enquadramento da ficha.',
            'arquivos': {'00-ficha.md': '# Ficha\n\nIdeia confirmada pelo usuário.\n'},
        }
        payload.update(changes)
        return payload

    def decision(self, **changes):
        payload = {
            'tipo': 'decisao', 'contexto': 'Duas alternativas foram avaliadas.',
            'opcoes': ['H1', 'H2'], 'escolha': 'H2',
            'motivo': 'Atende à necessidade que priorizei.',
            'objetivo': 'Reduzir o esforço para atingir o propósito.',
            'evidencias': ['conselho/parecer-teste.md'],
            'dissenso': 'O membro refutador manteve ressalva.',
            'confianca': 'media',
            'reverteria': 'Novo caso que refute a hipótese.',
            'arquivos': {'00-ficha.md': '# Ficha\n\nH2 escolhida pelo usuário.\n'},
        }
        payload.update(changes)
        return payload

    def register(self, payload, **options):
        return self.registrar_module.registrar(self.root, self.session, payload, **options)

    def final_theme_fixture(self, theme=1):
        """Dossiê pronto para testar uma trava isolada, sem simular 70 conversas."""
        self.cli('estado.py', 'proposito', self.root, '--session', self.session,
                 '--texto', 'Ajudar a pessoa a compreender a prioridade de sua decisão.')
        state = self.state()
        for stage in (item for item in self.core.catalog() if item['tema'] == theme):
            state.update(tema=theme, subetapa=stage['id'], passo=1)
            for step in range(1, 11):
                self.core.complete_step(state, step, f'Fixture: evidência do passo {step}',
                                        origem='usuario' if step == 2 else None)
        self.core.save_state(self.root, state)
        self.register(self.checkpoint())

    def prepare_approval(self, **extra):
        args = ['preparar-aprovacao', self.root, '--session', self.session,
                '--tema', self.state()['tema']]
        if not extra:
            args.extend(['--validacao-integrada', 'conselho/validacao-integrada.md'])
        else:
            for key, value in extra.items():
                args.append('--' + key.replace('_', '-'))
                if value is not True:
                    args.append(value)
        self.cli('estado.py', *args)
        return self.state()['aprovacao_pendente']

    def approve(self, pending, *, response='sim', token=None, caveat=None, success=True):
        args = ['aprovar', self.root, '--session', self.session, '--tema', pending['tema'],
                '--token', token or pending['token'], '--resposta', response,
                '--commit', pending['commit']]
        if caveat:
            args.extend(['--ressalva', caveat])
        return self.cli('estado.py', *args, success=success)

    @staticmethod
    def approved(value, *, origin='sintese_aprovada', reference='D-QA-APROVACAO'):
        return {'valor': value, 'aprovado': True, 'origem': origin, 'referencia': reference}

    def brief_payload(self, **fields):
        return {
            'cartao': {
                'subetapa': self.state()['subetapa'], 'aprovado': True,
                'fonte': 'duble-local:qa',
                'conteudo': {'objetivo': 'Explorar alternativas para o propósito.',
                             'entregar': 'Alternativas independentes com critérios.'},
            },
            'conteudo_aprovado': {'proposito': self.approved('Compreender a prioridade.'),
                                  **fields},
        }

    def make_brief(self, role, payload, **options):
        return self.brief.build_brief(self.root, role, payload, modo_teste=True, **options)

    def test_init_preserves_existing_dossier_and_history(self):
        before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
        self.cli('dossie_init.py', self.root, '--projeto', 'Outro nome', success=False)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)

    def test_init_refuses_nonempty_unrelated_directory(self):
        path = self.base / 'outro'
        path.mkdir()
        sentinel = path / 'nao-perder.txt'
        sentinel.write_text('trabalho pré-existente')
        self.cli('dossie_init.py', path, '--projeto', 'Outro', success=False)
        self.assertEqual(sentinel.read_text(), 'trabalho pré-existente')
        self.assertFalse((path / 'estado.json').exists())

    def test_init_creates_dedicated_git_and_valid_state(self):
        self.core.validate_state(self.state())
        self.assertEqual(Path(self.git('rev-parse', '--show-toplevel')), self.root)
        self.assertTrue((self.root / 'AGENTS.md').is_file())
        self.assertTrue((self.root / 'CLAUDE.md').is_file())
        self.assertTrue((self.root / '06-cir.md').is_file())

    def test_schema_rejects_invalid_types_and_unknown_steps(self):
        for changes in ({'tema': 'seis'}, {'tema': True}, {'tema': 7}, {'passo': 11},
                        {'pendencias': 'nenhuma'}, {'historico_ciclo': []}):
            with self.subTest(changes=changes):
                invalid = copy.deepcopy(self.state())
                invalid.update(changes)
                with self.assertRaises(self.core.CirError):
                    self.core.validate_state(invalid)

    def test_invalid_state_is_not_written(self):
        original = (self.root / 'estado.json').read_bytes()
        state = self.state()
        state['passo'] = -1
        with self.assertRaises(self.core.CirError):
            self.core.save_state(self.root, state)
        self.assertEqual((self.root / 'estado.json').read_bytes(), original)

    def test_stale_revision_cannot_overwrite_a_newer_state(self):
        first, stale = self.state(), self.state()
        first['projeto'] = 'Primeira atualização'
        self.core.save_state(self.root, first)
        before = (self.root / 'estado.json').read_bytes()
        stale['projeto'] = 'Atualização perdida'
        with self.assertRaises(self.core.CirError):
            self.core.save_state(self.root, stale)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)

    def test_second_session_cannot_write_or_release_first_session_lock(self):
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'lock', self.root, '--session', 'sessao-B', success=False)
        self.cli('estado.py', 'passo', self.root, '--session', 'sessao-B',
                 '--numero', 1, '--evidencia', 'Tentativa concorrente', success=False)
        self.cli('estado.py', 'unlock', self.root, '--session', 'sessao-B', success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)
        self.core.require_lock(self.root, self.session)
        self.cli('estado.py', 'unlock', self.root, '--session', self.session)
        self.cli('estado.py', 'lock', self.root, '--session', 'sessao-B')
        self.core.require_lock(self.root, 'sessao-B')

    def test_step_seven_requires_recorded_user_version(self):
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'passo', self.root, '--session', self.session,
                 '--numero', 7, '--evidencia', 'Alternativas', success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)

    def test_step_nine_requires_recorded_validation(self):
        self.complete_steps(7)
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'passo', self.root, '--session', self.session,
                 '--numero', 9, '--evidencia', 'Escolha', success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)

    def test_step_ten_is_owned_by_register_not_state_cli(self):
        self.complete_steps(9)
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'passo', self.root, '--session', self.session,
                 '--numero', 10, '--evidencia', 'Registro sem commit', success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)

    def test_approval_requires_prepared_context_not_only_word_sim(self):
        self.final_theme_fixture()
        head = self.git('rev-parse', 'HEAD')
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'aprovar', self.root, '--session', self.session,
                 '--tema', 1, '--token', 'sem-pergunta-contextual', '--resposta', 'sim',
                 '--commit', head, success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)

    def test_uncommitted_semantic_state_cannot_be_submitted_as_old_commit(self):
        self.final_theme_fixture()
        self.cli('estado.py', 'proposito', self.root, '--session', self.session,
                 '--texto', 'Propósito alterado depois do commit da versão.')
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'preparar-aprovacao', self.root, '--session', self.session,
                 '--tema', 1, '--validacao-integrada', 'conselho/validacao-integrada.md',
                 success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)

    def test_ok_silence_and_wrong_token_do_not_open_gate(self):
        self.final_theme_fixture()
        pending = self.prepare_approval()
        before = (self.root / 'estado.json').read_bytes()
        for response in ('ok', '', 'podemos continuar', 'sim, mas a outra pergunta'):
            with self.subTest(response=response):
                self.approve(pending, response=response, success=False)
                self.assertEqual((self.root / 'estado.json').read_bytes(), before)
        self.approve(pending, token='token-de-outra-pergunta', success=False)
        self.assertEqual(self.state()['travas']['1']['estado'], 'pendente')

    def test_contextual_approval_is_versioned_and_reservations_remain_pending(self):
        self.final_theme_fixture()
        pending = self.prepare_approval()
        self.approve(pending, caveat='Conferir o contraexemplo antes do CIR final.')
        approval = self.state()['travas']['1']
        self.assertEqual(approval['estado'], 'aprovado')
        self.assertEqual(approval['commit'], pending['commit'])
        self.assertEqual(self.git('cat-file', '-t', approval['commit']), 'commit')
        self.assertEqual(approval['resposta'], 'sim')
        self.assertTrue(approval['ressalvas'])
        self.assertTrue(self.state()['pendencias'])
        self.register(self.checkpoint(escolha='Registrar aprovação contextual do tema 1.'))
        committed_state = json.loads(self.git('show', 'HEAD:estado.json'))
        self.assertEqual(committed_state['travas']['1']['commit'], pending['commit'])
        self.assertEqual(committed_state['historico_ciclo']['1.7'][-1]['passo'], 10)

    def test_changed_artifact_invalidates_prepared_approval(self):
        self.final_theme_fixture()
        pending = self.prepare_approval()
        (self.root / '00-ficha.md').write_text('# Ficha alterada\n\nO conteúdo mudou após a pergunta.\n')
        self.approve(pending, success=False)
        self.assertEqual(self.state()['travas']['1']['estado'], 'pendente')

    def test_manual_decision_log_edit_invalidates_prepared_approval(self):
        self.final_theme_fixture()
        pending = self.prepare_approval()
        path = self.root / 'decisoes.md'
        path.write_text(path.read_text() + '\nContexto alterado manualmente após a pergunta.\n')
        before = (self.root / 'estado.json').read_bytes()
        self.approve(pending, success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)
        self.assertEqual(self.state()['travas']['1']['estado'], 'pendente')

    def test_gate_cannot_advance_without_user_approval(self):
        self.final_theme_fixture()
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'avancar', self.root, '--session', self.session, success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)

    def test_approval_without_integrated_validation_records_reason_and_risk(self):
        self.final_theme_fixture()
        self.cli('estado.py', 'preparar-aprovacao', self.root, '--session', self.session,
                 '--tema', 1, '--sem-validacao', success=False)
        pending = self.prepare_approval(
            sem_validacao=True, risco='A integração não foi examinada.',
            motivo='Preciso continuar a exploração neste momento.',
            objetivo='Testar o enquadramento antes de investir mais.',
        )
        self.approve(pending)
        state = self.state()
        self.assertTrue(state['travas']['1']['sem_validacao_integrada'])
        self.assertEqual(state['travas']['1']['risco'], 'A integração não foi examinada.')
        self.assertTrue(any('sem validação integrada' in item['origem'] for item in state['pendencias']))

    def test_approval_requires_its_own_commit_before_crossing_gate(self):
        self.final_theme_fixture()
        pending = self.prepare_approval()
        self.approve(pending)
        self.cli('estado.py', 'avancar', self.root, '--session', self.session, success=False)
        self.register(self.checkpoint())
        self.cli('estado.py', 'avancar', self.root, '--session', self.session)
        self.assertEqual(self.state()['subetapa'], '2.1')

    def test_artifact_changed_after_approval_requires_new_approval(self):
        self.final_theme_fixture()
        self.approve(self.prepare_approval())
        self.register(self.checkpoint())
        self.register(self.checkpoint(arquivos={
            '00-ficha.md': '# Ficha\n\nNova descrição acrescentada após a aprovação.\n'
        }))
        self.cli('estado.py', 'avancar', self.root, '--session', self.session, success=False)
        self.assertEqual(self.state()['subetapa'], '1.7')

    def test_frozen_purpose_change_requires_explicit_reopening(self):
        self.final_theme_fixture()
        self.approve(self.prepare_approval())
        self.register(self.checkpoint())
        before = (self.root / 'estado.json').read_bytes()
        self.cli('estado.py', 'proposito', self.root, '--session', self.session,
                 '--texto', 'Um propósito diferente.', success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)
        self.cli('estado.py', 'reabrir', self.root, '--session', self.session,
                 '--texto', 'Um propósito diferente.', success=False)
        self.assertEqual((self.root / 'estado.json').read_bytes(), before)
        self.cli('estado.py', 'reabrir', self.root, '--session', self.session,
                 '--texto', 'Compreender outra necessidade mais ampla.',
                 '--motivo', 'Descobri que o enquadramento anterior era restrito.',
                 '--objetivo', 'Reexaminar a necessidade que orienta o projeto.',
                 '--risco', 'Revisar as decisões derivadas do propósito anterior.')
        state = self.state()
        self.assertEqual(state['subetapa'], '1.1')
        self.assertIsNone(state['proposito']['congelado_em'])
        self.assertEqual(state['proposito']['hash'], self.core.sha256_text(state['proposito']['texto']))
        self.assertTrue(all(item['estado'] == 'reaberto' for item in state['travas'].values()))
        self.assertTrue(state['pendencias'])
        self.assertTrue(state['ciclos_anteriores'])
        self.assertFalse(any(identifier.startswith('1.') for identifier in state['subetapas_concluidas']))

    def test_vigia_detects_manual_edit_of_frozen_purpose_artifact(self):
        self.final_theme_fixture()
        self.approve(self.prepare_approval())
        self.assertTrue(self.vigia.scan_project(self.root)['proposito_integro'])
        (self.root / '01-proposito.md').write_text('# Propósito\n\nTexto diferente sem reabertura.\n')
        result = self.vigia.scan_project(self.root)
        self.assertFalse(result['proposito_integro'])
        self.assertTrue(any(item['sinal'] == 'proposito_artefato_divergente'
                            for item in result['alertas']))

    def test_fresh_dossier_is_not_ready(self):
        result = self.pendencias.check_project(self.root)
        self.assertIs(result['pronto'], False)
        self.assertTrue(result.get('checklist') or result.get('artefatos_invalidos'))

    def test_placeholders_do_not_count_as_substantive_artifacts(self):
        for placeholder in ('# CIR\n\nPENDENTE\n', '# Prova\n\n- Resultado: a preencher\n',
                            '# Pronto\n\n<!-- modelo -->\n- [ ] A definir\n'):
            with self.subTest(placeholder=placeholder):
                self.assertFalse(self.vigia.meaningful_text(placeholder))
        self.assertTrue(self.vigia.meaningful_text('# Ficha\n\nA pessoa quer compreender a prioridade.'))

    def test_open_reservation_remains_a_readiness_blocker(self):
        self.update_state(pendencias=[{
            'id': 'P-QA', 'origem': 'Aprovação com ressalva',
            'risco': 'Falta caso contraexemplo', 'exigida_no_pronto': True,
            'estado': 'aberta',
        }])
        result = self.pendencias.check_project(self.root)
        self.assertIs(result['pronto'], False)
        self.assertTrue(any(item['id'] == 'P-QA' for item in result['pendencias_abertas']))

    def test_readiness_revokes_attestation_after_evidence_changes(self):
        path = self.root / 'fontes' / 'evidencia-qa.md'
        path.write_text('# Revisão\n\nO documento foi examinado em sessão independente.\n')
        item = {
            'atestado': True, 'revisado_por': 'revisor-qa',
            'revisado_em': '2026-10-23T12:00:00+00:00',
            'observacao': 'As condições deste item foram verificadas na evidência vinculada.',
            'evidencias': [{'arquivo': 'fontes/evidencia-qa.md',
                            'sha256': self.core.sha256_text(path.read_text())}],
        }
        (self.root / 'evidencias-pronto.json').write_text(json.dumps({'itens': {'1': item}}))
        initial = self.pendencias.check_project(self.root)
        self.assertTrue(initial['checklist'][0]['atestado'])
        self.assertFalse(initial['pronto'])  # Os outros 13 itens continuam ausentes.
        path.write_text('# Revisão\n\nA evidência foi alterada depois da revisão.\n')
        changed = self.pendencias.check_project(self.root)
        self.assertFalse(changed['checklist'][0]['atestado'])
        self.assertFalse(changed['pronto'])

    def test_readiness_does_not_accept_checkmarks_without_evidence(self):
        (self.root / '06-pronto.md').write_text('# Pronto\n\n' + '- [x] Atendido\n' * 14)
        (self.root / 'evidencias-pronto.json').write_text(json.dumps({
            'itens': {str(number): {'atestado': True} for number in range(1, 15)}
        }))
        result = self.pendencias.check_project(self.root)
        self.assertFalse(result['pronto'])
        self.assertTrue(all(not item['atestado'] for item in result['checklist']))

    def test_vigia_reports_committed_product_prescriptions_and_respects_routing(self):
        text = 'Vamos lançar o MVP primeiro por R$ 99. Usaremos React na solução.'
        alerts = self.vigia.scan_text(text, path='06-cir.md', state={'tema': 3})
        self.assertTrue(alerts)
        self.assertTrue(any(item['sinal'] == 'recorte_de_produto' for item in alerts))
        self.assertTrue(any(item['sinal'] == 'criterio_comercial_no_cir' for item in alerts))
        self.assertEqual(self.vigia.scan_text(text, path='estacionamento.md', state={'tema': 3}), [])
        self.assertEqual(self.vigia.scan_text('Preço não é critério nesta etapa.',
                                             path='06-cir.md', state={'tema': 3}), [])

    def test_vigia_rejects_symlink_and_traversal_sources(self):
        outside = self.base / 'fonte-externa.md'
        outside.write_text('MARCADOR_EXTERNO_PRIVADO')
        linked = self.root / 'fontes' / 'vazada.md'
        linked.symlink_to(outside)
        for relative in ('../fonte-externa.md', 'fontes/vazada.md'):
            with self.subTest(relative=relative):
                with self.assertRaises(self.core.CirError):
                    self.vigia.scan_project(self.root, paths=[relative])

    def test_generator_brief_requires_recorded_second_step(self):
        with self.assertRaises(self.core.CirError):
            self.make_brief('gerador', self.brief_payload())
        self.complete_steps(2)
        result = self.make_brief('gerador', self.brief_payload())
        self.assertEqual(result['para'], 'gerador')
        self.assertEqual(result['conteudo']['proposito'], 'Compreender a prioridade.')

    def test_generator_brief_excludes_user_authorship_bank_and_reserved_markers(self):
        self.complete_steps(2)
        markers = {
            'versao_usuario': 'VERSAO_USUARIO_PRIVADA_QA_913',
            'autoria': 'AUTORIA_PRIVADA_QA_927',
            'banco': 'BANCO_PRIVADO_QA_948',
            'casos_reservados': 'RESERVADO_PRIVADO_QA_962',
        }
        payload = self.brief_payload()
        payload.update(markers)
        payload['conteudo_aprovado'].update(markers)
        serialized = json.dumps(self.make_brief('gerador', payload), ensure_ascii=False)
        for marker in markers.values():
            self.assertNotIn(marker, serialized)

    def test_reserved_case_is_hidden_before_theme_five_and_available_for_evaluation(self):
        marker = 'CASO_RESERVADO_QA_984'
        payload = self.brief_payload(casos_de_avaliacao=self.approved(
            marker, origin='artefato_anonimizado'))
        first = self.make_brief('conselho', payload)
        self.assertNotIn(marker, json.dumps(first))
        self.update_state(tema=5, subetapa='5.1', passo=1)
        second = self.make_brief('conselho', self.brief_payload(
            casos_de_avaliacao=self.approved(marker, origin='artefato_anonimizado')))
        self.assertIn(marker, json.dumps(second))

    def test_authorship_marker_cannot_leak_through_approval_reference(self):
        marker = 'AUTORIA_QA_SECRETA_109'
        payload = self.brief_payload(proposito=self.approved(
            'Priorizar a compreensão.', reference=marker))
        payload['autoria'] = marker
        with self.assertRaises(self.core.CirError):
            self.make_brief('conselho', payload)

    def test_reserved_marker_repeated_in_allowed_content_is_rejected(self):
        marker = 'RESERVADO_QA_SECRETO_183'
        payload = self.brief_payload(proposito=self.approved(marker))
        payload['casos_reservados'] = marker
        with self.assertRaises(self.core.CirError):
            self.make_brief('conselho', payload)

    def test_context_requires_explicit_approval_and_generator_safe_origin(self):
        self.complete_steps(2)
        for envelope in (
            {'valor': 'Sem aprovação', 'aprovado': False},
            self.approved('Versão livre', origin='artefato_anonimizado'),
        ):
            with self.subTest(envelope=envelope):
                with self.assertRaises(self.core.CirError):
                    self.make_brief('gerador', self.brief_payload(proposito=envelope))

    def test_nested_authorship_in_allowed_hypotheses_is_rejected(self):
        payload = self.brief_payload(hipoteses=self.approved(
            [{'id': 'H1', 'autoria': 'AUTORIA_ANINHADA_SECRETA'}],
            origin='artefato_anonimizado'))
        with self.assertRaises(self.core.CirError):
            self.make_brief('conselho', payload)

    def test_second_council_round_can_include_anonymous_arguments_only(self):
        marker = 'ARGUMENTO_ANONIMO_QA'
        payload = self.brief_payload(argumentos_anonimos=self.approved(
            marker, origin='artefato_anonimizado'))
        first = self.make_brief('conselho', payload, rodada=1)
        second = self.make_brief('conselho', payload, rodada=2)
        self.assertNotIn(marker, json.dumps(first))
        self.assertIn(marker, json.dumps(second))

    def test_doubles_require_explicit_test_mode(self):
        with self.assertRaises(self.core.CirError):
            self.brief.build_brief(self.root, 'conselho', self.brief_payload())
        result = self.make_brief('conselho', self.brief_payload())
        self.assertEqual(result['modo'], 'teste_local')

    def test_unimplemented_method_card_is_never_assumed_available(self):
        self.update_state(tema=2, subetapa='2.3', passo=1)
        with self.assertRaises(self.core.CirError):
            self.make_brief('conselho', {'conteudo_aprovado': {}})

    def test_checkpoint_is_committed_without_marking_cycle_complete(self):
        before = self.git('rev-parse', 'HEAD')
        self.register(self.checkpoint())
        after = self.git('rev-parse', 'HEAD')
        self.assertNotEqual(after, before)
        self.assertIn('Ideia confirmada pelo usuário.', self.git('show', 'HEAD:00-ficha.md'))
        self.assertEqual(self.state()['passo'], 1)
        self.assertNotIn('0.1', self.state()['subetapas_concluidas'])
        self.assertFalse((self.root / '.registro-pendente.json').exists())

    def test_decision_requires_validation_and_completes_tenth_step_with_commit(self):
        head = self.git('rev-parse', 'HEAD')
        with self.assertRaises(self.core.CirError):
            self.register(self.decision())
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.complete_steps(9)
        self.register(self.decision())
        state = self.state()
        self.assertIn('0.1', state['subetapas_concluidas'])
        self.assertEqual([event['passo'] for event in state['historico_ciclo']['0.1']],
                         list(range(1, 11)))
        record = self.git('show', 'HEAD:decisoes.md')
        for text in ('H2', 'Atende à necessidade', 'Reduzir o esforço'):
            self.assertIn(text, record)

    def test_nonbinary_decision_requires_users_reason_and_objective(self):
        self.complete_steps(9)
        before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
        for field in ('motivo', 'objetivo'):
            with self.subTest(field=field):
                invalid = self.decision()
                invalid[field] = ''
                with self.assertRaises(self.core.CirError):
                    self.register(invalid)
                self.assertEqual(self.snapshot(), before)
                self.assertEqual(self.git('rev-parse', 'HEAD'), head)

    def test_decision_without_recorded_dose_cannot_complete_substage(self):
        self.update_state(doses={})
        self.complete_steps(9)
        before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
        with self.assertRaises(self.core.CirError):
            self.register(self.decision())
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertNotIn('0.1', self.state()['subetapas_concluidas'])

    def test_recorded_decisions_are_not_treated_as_empty_template(self):
        self.complete_steps(9)
        self.register(self.decision())
        text = (self.root / 'decisoes.md').read_text()
        self.assertTrue(self.vigia.meaningful_text(text))
        self.assertIn('Motivo nas palavras do usuário', text)
        self.assertIn('H2', text)

    def test_commit_failure_restores_documents_and_state(self):
        before = self.snapshot()
        head = self.git('rev-parse', 'HEAD')
        real_git = self.registrar_module.run_git

        def fail_commit(root, *args):
            if 'commit' in args:
                raise self.core.CirError('Falha simulada de commit')
            return real_git(root, *args)

        with mock.patch.object(self.registrar_module, 'run_git', side_effect=fail_commit):
            with self.assertRaises(self.core.CirError):
                self.register(self.checkpoint())
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), '')

    def test_crash_before_commit_can_be_recovered_without_losing_prior_work(self):
        before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
        real_git = self.registrar_module.run_git

        def interrupt_commit(root, *args):
            if 'commit' in args:
                raise KeyboardInterrupt('Interrupção simulada')
            return real_git(root, *args)

        with mock.patch.object(self.registrar_module, 'run_git', side_effect=interrupt_commit):
            with self.assertRaises(KeyboardInterrupt):
                self.register(self.checkpoint())
        self.assertTrue((self.root / '.registro-pendente.json').is_file())
        self.registrar_module.recuperar(self.root, self.session)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), '')

    def test_crash_after_commit_recovers_receipt_without_undoing_commit(self):
        before = self.git('rev-parse', 'HEAD')
        with mock.patch.object(self.registrar_module, 'receipt', side_effect=OSError('Disco indisponível')):
            with self.assertRaises(OSError):
                self.register(self.checkpoint())
        committed = self.git('rev-parse', 'HEAD')
        self.assertNotEqual(committed, before)
        self.assertTrue((self.root / '.registro-pendente.json').exists())
        result = self.registrar_module.recuperar(self.root, self.session)
        self.assertEqual(result['commit'], committed)
        self.assertEqual(self.git('rev-parse', 'HEAD'), committed)
        self.assertFalse((self.root / '.registro-pendente.json').exists())
        self.assertIn('Ideia confirmada', self.git('show', 'HEAD:00-ficha.md'))

    def test_recovery_preserves_manual_changes_made_after_interruption(self):
        head = self.git('rev-parse', 'HEAD')
        real_git = self.registrar_module.run_git

        def interrupt_commit(root, *args):
            if 'commit' in args:
                raise KeyboardInterrupt('Interrupção simulada')
            return real_git(root, *args)

        with mock.patch.object(self.registrar_module, 'run_git', side_effect=interrupt_commit):
            with self.assertRaises(KeyboardInterrupt):
                self.register(self.checkpoint())
        target = self.root / '00-ficha.md'
        edited = b'# Ficha\n\nManual correction after interruption: preserve this version.\n'
        target.write_bytes(edited)
        before = self.snapshot()
        with self.assertRaises(self.core.CirError):
            self.registrar_module.recuperar(self.root, self.session)
        self.assertEqual(target.read_bytes(), edited)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertTrue((self.root / '.registro-pendente.json').is_file())

    def test_recovery_preserves_state_edits_made_after_interruption(self):
        head = self.git('rev-parse', 'HEAD')
        real_git = self.registrar_module.run_git

        def interrupt_commit(root, *args):
            if 'commit' in args:
                raise KeyboardInterrupt('Interrupção simulada')
            return real_git(root, *args)

        with mock.patch.object(self.registrar_module, 'run_git', side_effect=interrupt_commit):
            with self.assertRaises(KeyboardInterrupt):
                self.register(self.checkpoint())
        self.update_state(projeto='Correção manual posterior à interrupção')
        before = self.snapshot()
        with self.assertRaises(self.core.CirError):
            self.registrar_module.recuperar(self.root, self.session)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertTrue((self.root / '.registro-pendente.json').is_file())

    def test_offline_push_preserves_local_commit_and_pending_receipt(self):
        self.git('remote', 'add', 'origin', self.base / 'remoto-ausente.git')
        before = self.git('rev-parse', 'HEAD')
        result = self.register(self.checkpoint(), push=True, confirmar_remoto_privado=True)
        after = self.git('rev-parse', 'HEAD')
        self.assertNotEqual(after, before)
        self.assertEqual(result['commit'], after)
        self.assertEqual(result['envio'], 'pendente')
        pending = json.loads((self.root / '.envio-pendente.json').read_text())
        self.assertEqual(pending['commit'], after)
        self.assertNotIn('.envio-pendente.json', self.git('ls-tree', '-r', '--name-only', 'HEAD'))
        self.registrar_module.recuperar(self.root, self.session)
        self.assertEqual(self.git('rev-parse', 'HEAD'), after)

    def test_staged_collateral_is_not_committed(self):
        path = self.root / 'segredo-colateral.txt'
        path.write_text('NÃO PUBLICAR')
        self.git('add', path.name)
        before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
        with self.assertRaises(self.core.CirError):
            self.register(self.checkpoint())
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(self.git('diff', '--cached', '--name-only'), path.name)

    def test_unstaged_collateral_is_not_committed(self):
        path = self.root / 'segredo-colateral.txt'
        path.write_text('NÃO PUBLICAR')
        before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
        with self.assertRaises(self.core.CirError):
            self.register(self.checkpoint())
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)
        self.assertEqual(path.read_text(), 'NÃO PUBLICAR')

    def test_register_rejects_traversal_absolute_paths_and_git_metadata(self):
        outside = self.base / 'externo.txt'
        outside.write_text('PRESERVAR')
        for destination in ('../externo.txt', str(outside), '.git/config',
                            'briefs/../../externo.txt', 'AGENTS.md', 'CLAUDE.md'):
            with self.subTest(destination=destination):
                before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
                with self.assertRaises(self.core.CirError):
                    self.register(self.checkpoint(arquivos={destination: 'SOBRESCREVER'}))
                self.assertEqual(self.snapshot(), before)
                self.assertEqual(self.git('rev-parse', 'HEAD'), head)
                self.assertEqual(outside.read_text(), 'PRESERVAR')

    def test_register_rejects_symlink_to_external_file(self):
        outside = self.base / 'externo.txt'
        outside.write_text('PRESERVAR')
        target = self.root / '00-ficha.md'
        target.unlink()
        target.symlink_to(outside)
        head = self.git('rev-parse', 'HEAD')
        with self.assertRaises(self.core.CirError):
            self.register(self.checkpoint())
        self.assertTrue(target.is_symlink())
        self.assertEqual(outside.read_text(), 'PRESERVAR')
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)

    def test_register_rejects_symlinked_directory(self):
        outside = self.base / 'externo'
        outside.mkdir()
        (self.root / 'fontes').rmdir()
        (self.root / 'fontes').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(self.core.CirError):
            self.register(self.checkpoint(arquivos={'fontes/ficha.md': 'NÃO ESCREVER'}))
        self.assertFalse((outside / 'ficha.md').exists())

    def test_recovery_with_no_pending_transaction_is_idempotent(self):
        before, head = self.snapshot(), self.git('rev-parse', 'HEAD')
        self.registrar_module.recuperar(self.root, self.session)
        self.registrar_module.recuperar(self.root, self.session)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.git('rev-parse', 'HEAD'), head)


if __name__ == '__main__':
    unittest.main()
