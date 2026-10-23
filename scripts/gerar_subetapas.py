#!/usr/bin/env python3
"""Gera o índice a partir de S08; não cria cartões de skills ausentes."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


def generate(repo: Path) -> tuple[str, str]:
    source = repo / "sources/originais/fluxograma-completo-ideal.md"
    text = source.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^#### (\d+\.\d+) ([^\n]+)$", text, re.M))
    if len(headings) != 51:
        raise ValueError(f"S08 deve conter 51 sub-etapas, encontradas {len(headings)}")
    cards = {
        "0.1": {
            "objetivo": "Registrar a ficha fiel à ideia e às palavras do usuário, sem interpretar.",
            "grill": "Ideia, motivo, vocabulário, limites e resultado esperado desta etapa.",
            "pesquisa": "Visão geral do fenômeno para evitar perguntas óbvias; conferir as fontes citadas.",
            "refuta_se": "O usuário não reconhece sua ideia ou falta algo que disse.",
            "entregar": "00-ficha.md, com confirmação do usuário.",
        },
        "0.2": {
            "objetivo": "Classificar material existente entre Etapas 1, 2, 3 e ideias de solução.",
            "grill": "Situação do material e decisões que o usuário considera intocáveis.",
            "pesquisa": "Conferir afirmações centrais do material que alimentará o mapa.",
            "refuta_se": "Material de Etapa 2 ou 3 ficou como Etapa 1, ou solução virou requisito.",
            "entregar": "00-separacao.md; encaminhamentos com origem e motivo.",
        },
        "0.3": {
            "objetivo": "Preparar dossiê, doses, mapa de modelos e restrições de confidencialidade.",
            "grill": "Modelos por papel, acompanhamento das sessões, material sigiloso e destinos proibidos.",
            "pesquisa": "Conferir capacidades e disponibilidade efetivas do ambiente.",
            "refuta_se": "Falta escolha de modelos ou as restrições de confidencialidade não estão registradas.",
            "entregar": "Estado inicial e mapa de modelos aprovado.",
        },
    }
    items = []
    for index, match in enumerate(headings):
        identifier, heading = match.groups()
        theme = int(identifier.split(".")[0])
        title = heading.split(" · ")[0]
        dose_match = re.search(r"dose (leve|padrão|completa)", heading)
        dose = {"leve": "leve", "padrão": "padrao", "completa": "completa"}.get(
            dose_match.group(1) if dose_match else "", "completa"
        )
        skill = {
            0: "etapa-1-cir", 1: "cir-proposito", 2: "cir-mapa",
            3: "cir-idealidade", 5: "cir-prova", 6: "cir-sintese",
        }.get(theme)
        if theme == 4:
            skill = "cir-divergencia" if int(identifier.split(".")[1]) <= 7 else "cir-arquitetura"
        previous = [headings[index - 1].group(1)] if index else []
        prerequisite_source = "editorial: predecessor no percurso completo; não substitui dependências do cartão"
        if identifier == "2.3":
            previous = ["2.1", "2.2"]
            prerequisite_source = "S10 §9: exemplo explícito do cartão de 2.3"
        items.append({
            "id": identifier, "titulo": title, "tema": theme, "dose": dose,
            "dose_origem": "S08: título" if dose_match else "editorial: dose completa para fechamento/aprovação integrada; ajustável por S10 §6.7",
            "trava": identifier in {"1.7", "3.6", "5.7", "6.6"},
            "tema_com_trava": theme in {1, 3, 5, 6}, "skill": skill,
            "pre_requisitos": previous, "pre_requisitos_origem": prerequisite_source,
            "cartao_disponivel": theme == 0,
            "cartao_origem": "S10 §6.2 + S08 §3; operacionalização editorial" if theme == 0 else "ausente: depende da skill de método",
            "cartao": cards.get(identifier),
            "fonte": {"id": "S08", "secao": "3", "linha": text[:match.start()].count("\n") + 1},
        })
    data = {
        "schema_version": 1,
        "origem": "S08 §3; S10 §§6.2 e 9–10",
        "fonte_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "nota": "Índice editorial de 51 sub-etapas. Não instala nem substitui as sete skills de método. Cartões dos temas 1–6 indisponíveis.",
        "subetapas": items,
    }
    rows = [
        "# Índice das sub-etapas", "",
        "Gerado por `scripts/gerar_subetapas.py`, na raiz do repositório de desenvolvimento, a partir de S08 §3 e S10 §§6.2, 9–10. Não editar manualmente.", "",
        "São 51 sub-etapas. As skills de método dos temas 1–6 e seus cartões ainda estão indisponíveis; este índice não as implementa. A condutora pode receber um cartão externo aprovado, preservando a procedência.", "",
        "As doses com asterisco são escolhas editoriais para fechamentos integrados cujo título não fixa dose. Pré-requisitos são o predecessor do percurso completo, uma aproximação editorial para conferência inicial; 2.3 usa os pré-requisitos explícitos de S10 §9. Um cartão real pode declarar dependências mais precisas.", "",
        "| ID | Sub-etapa | Dose | Trava | Skill | Pré-requisitos | Cartão |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in items:
        dose_label = item["dose"] + ("*" if not item["dose_origem"].startswith("S08") else "")
        rows.append(f"| {item['id']} | {item['titulo']} | {dose_label} | {'sim' if item['trava'] else '—'} | `{item['skill']}` | {', '.join(item['pre_requisitos']) or '—'} | {'tema 0' if item['cartao_disponivel'] else 'ausente'} |")
    rows += ["", "A confirmação da ficha 0.1 é exigida, embora não seja uma das quatro travas formais. Nos temas 2 e 4, saltos ficam registrados; 4.9 e 4.11 continuam exigindo conselho. Fontes completas preservadas em `sources/originais/` no repositório.", ""]
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n", "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="confere sem gravar")
    args = parser.parse_args()
    generated = generate(args.repo.resolve())
    base = args.repo / "skills/etapa-1-cir"
    paths = [base / "assets/subetapas.json", base / "references/subetapas.md"]
    for path, value in zip(paths, generated):
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != value:
                print(f"Desatualizado: {path}")
                return 1
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8")
    print("Índice de 51 sub-etapas conferido." if args.check else "Índice de 51 sub-etapas gerado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
