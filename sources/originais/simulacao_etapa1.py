"""
Simulação de variantes da Etapa 1 (Concepção Ideal) — modelo de brinquedo.
Os números saem das premissas abaixo. O objetivo não é prever, e sim ver quais
conclusões sobrevivem quando as premissas variam em faixas amplas.

Uma solução tem dois tipos de componente que afetam o propósito:
  núcleo  (ex.: a análise)  e  cadeia (o que faz o resultado acontecer na vida da
  pessoa: entrega, prioridade, compreensão, confiança, esforço).
Idealidade Q = núcleo^(1-w) * cadeia^w  (w = quanto o propósito depende da cadeia humana)
Enfeites e jobs adjacentes não mudam Q, mas algumas ideias tangenciais escondem uma
função valiosa ("surpresa") e algumas ideias de experiência são anti-ideais (parecem
boas, mas pioram o propósito, como priorizar pelo que a pessoa quer ver).

Uso: python3 simulacao_etapa1.py [n_rodadas]   (padrão 6000; leva ~30 s)
Variantes: V1 só núcleo | V2 propósito sem tangentes | V3 divergência máxima com CIR amplo |
V4 divergência ampla com CIR estreito | V5 CIR amplo elaborado e depois convergido |
V4+A avaliação extra | V4+R rodada extra de ideias |
IDEAL esboço integrado curto + triagem + avaliação forte (a configuração do método).
"""
import numpy as np, json, sys

C_IDEA, C_ABS, C_ELAB, C_EVAL, FIXO = 0.15, 0.05, 0.4, 3.0, 3.0   # dias

def params(rng, **fix):
    P = dict(w=rng.uniform(0, .8), sigma=rng.uniform(.05, .30), p_s=rng.uniform(0, .15),
             p_h=rng.uniform(0, .25), h=rng.uniform(.1, .5), d=rng.uniform(.4, .9),
             r=rng.uniform(.4, .9), m=rng.uniform(1, 6), c_comp=rng.uniform(5, 20),
             u=rng.uniform(.2, .6), g=rng.uniform(.2, .7), dil=rng.uniform(0, .04),
             A=rng.uniform(30, 300))
    P.update(fix); return P

def gerar(rng, P, n_core, n_chain, n_del, n_adj):
    I = {}
    I['core'] = rng.beta(2, 4, n_core)
    q = rng.beta(2, 4, n_chain); harm = rng.random(n_chain) < P['p_h']
    I['chain'], I['chain_harm'] = q, harm
    I['chain_look'] = np.where(harm, rng.beta(4, 2, n_chain), q)          # dano parece bom
    n_t = n_del + n_adj
    kind = np.array([0]*n_del + [1]*n_adj)                                # 0 enfeite, 1 adjacente
    appeal = rng.beta(2, 4, n_t); surpr = rng.random(n_t) < P['p_s']
    latent = rng.beta(5, 2, n_t); to_core = rng.random(n_t) < .3
    harm_t = (kind == 0) & (rng.random(n_t) < P['p_h']) & ~surpr
    look = np.where(harm_t, np.maximum(appeal, rng.beta(4, 2, n_t)),
                    np.where(surpr, np.maximum(appeal, .8*latent), appeal))
    I.update(t_kind=kind, t_appeal=appeal, t_surpr=surpr, t_latent=latent, t_core=to_core,
             t_harm=harm_t, t_look=look)
    return I

def ruido(rng, x, s): return x + rng.normal(0, s, len(x))

def escolher(rng, true, look, s):
    if len(true) == 0: return None
    return int(np.argmax(ruido(rng, look, s)))

def Qf(core, chain, w, add=False):
    return (1-w)*core + w*chain if add else core**(1-w) * chain**w

def v1(rng, P, N=30, add=False):              # núcleo estrito; cadeia feita tarde
    I = gerar(rng, P, N, 0, 0, 0)
    core = I['core'][escolher(rng, I['core'], I['core'], P['sigma'])]
    L = gerar(rng, P, 0, 3, 0, 0)                # cadeia improvisada na etapa 2/3
    k = escolher(rng, L['chain'], L['chain_look'], P['sigma'])
    harm = L['chain_harm'][k]; chain = L['chain'][k]
    Q = Qf(core, chain, P['w'], add) * ((1-P['h']) if harm else 1)
    retrab = (rng.random() < P['w']) * P['m'] * 5
    T1 = FIXO + N*C_IDEA
    T = T1 + 2*P['c_comp'] + 3*C_IDEA + retrab
    rep = int((I['core'] > .6).sum())
    return dict(Q=Q, T=T, T1=T1, comps=2, rep=rep, surp=0, dano=int(harm))

def foco(rng, P, I, s, d, add=False, extra_T=0.0, tang=False, r=None):
    """Convergência com teste de propósito. tang=True: abstrai ideias tangenciais."""
    cand_core_t, cand_core_l = list(I['core']), list(I['core'])
    keep = ~(I['chain_harm'] & (rng.random(len(I['chain'])) < d))
    ch_t = list(I['chain'][keep]); ch_l = list(I['chain_look'][keep]); ch_h = list(I['chain_harm'][keep])
    surp = 0
    if tang:
        rec = I['t_surpr'] & (rng.random(len(I['t_surpr'])) < r)
        surp = int(rec.sum())
        for j in np.where(rec)[0]:
            if I['t_core'][j]: cand_core_t.append(I['t_latent'][j]); cand_core_l.append(I['t_latent'][j])
            else: ch_t.append(I['t_latent'][j]); ch_l.append(I['t_latent'][j]); ch_h.append(False)
    kc = escolher(rng, np.array(cand_core_t), np.array(cand_core_l), s)
    kh = escolher(rng, np.array(ch_t), np.array(ch_l), s)
    core = cand_core_t[kc]
    chain, harm = (ch_t[kh], ch_h[kh]) if kh is not None else (.2, False)   # sem candidata: cadeia genérica
    Q = Qf(core, chain, P['w'], add) * ((1-P['h']) if harm else 1)
    good = (I['core'] > .6).sum() + (I['chain'][~I['chain_harm']] > .6).sum()
    if tang: good += surp + ((I['t_appeal'] > .6) & ~I['t_harm']).sum()
    n = len(I['core']) + len(I['chain']) + len(I['t_kind'])
    T1 = FIXO + n*C_IDEA + (len(I['t_kind'])*C_ABS if tang else 0) + extra_T
    return dict(Q=Q, T=T1 + 2*P['c_comp'], T1=T1, comps=2, rep=int(good), surp=surp, dano=int(harm))

def aloc(N, share):                           # divide N ideias: núcleo/cadeia e tangenciais
    n_t = int(round(N*share)); n_f = N - n_t
    n_core = int(round(n_f*.55)); return n_core, n_f-n_core, n_t//2, n_t-n_t//2

def v2(rng, P, N=30, add=False):              # foco no propósito (núcleo + cadeia), sem tangentes
    I = gerar(rng, P, *aloc(N, 0)); return foco(rng, P, I, P['sigma'], P['d'], add)

def v3(rng, P, I, add=False):                 # divergência máxima, tudo que parece bom entra no CIR
    s = P['sigma']; tau = .55
    kc = escolher(rng, I['core'], I['core'], s); core = I['core'][kc]
    kh = escolher(rng, I['chain'], I['chain_look'], s)
    inc_ch = ruido(rng, I['chain_look'], s) > tau; inc_ch[kh] = True
    inc_t = ruido(rng, I['t_look'], s) > tau
    chain = float(I['chain'][inc_ch].max())
    for j in np.where(inc_t & I['t_surpr'])[0]:            # surpresa entra como forma, não função
        if I['t_core'][j]: core = max(core, .6*I['t_latent'][j])
        else: chain = max(chain, .6*I['t_latent'][j])
    n_harm = int((inc_ch & I['chain_harm']).sum() + (inc_t & I['t_harm']).sum())
    extras = int(inc_ch.sum() - 1 + inc_t.sum()); comps = 2 + extras
    Q = Qf(core, chain, P['w'], add) * (1-P['h'])**n_harm * max(0, 1 - P['dil']*extras)
    n = len(I['core']) + len(I['chain']) + len(I['t_kind'])
    T1 = FIXO + n*C_IDEA
    T = T1 + 2*P['c_comp'] + extras*P['c_comp']*P['u']
    rep = (I['core'] > .6).sum() + (I['chain'][~I['chain_harm']] > .6).sum() + ((I['t_appeal'] > .6) & ~I['t_harm']).sum()
    return dict(Q=Q, T=T, T1=T1, comps=comps, rep=int(rep), surp=0, dano=int(n_harm > 0))

def v4(rng, P, I, add=False):                 # divergência ampla, CIR estreito, estacionamento
    return foco(rng, P, I, P['sigma'], P['d'], add, tang=True, r=P['r'])

def v5(rng, P, I, add=False):                 # sua proposta: CIR amplo elaborado -> convergência
    s = P['sigma']; n_el = int((ruido(rng, I['chain_look'], s) > .55).sum() + (ruido(rng, I['t_look'], s) > .55).sum()) + 2
    g = P['g']
    return foco(rng, P, I, s*(1-.5*g), P['d'] + (1-P['d'])*g, add, extra_T=n_el*C_ELAB,
                tang=True, r=P['r'] + (1-P['r'])*g)

def v4a(rng, P, I, add=False):                # + etapa extra de avaliação (casos canônicos, red team)
    return foco(rng, P, I, P['sigma']*.5, P['d'] + (1-P['d'])*.5, add, extra_T=C_EVAL, tang=True, r=P['r'])

def v_ideal(rng, P, I, add=False):            # IDEAL: esboço integrado curto (passo 5) + triagem (6) + avaliação forte (8)
    s = P['sigma']; g = .6*P['g']
    n_el = int((ruido(rng, I['chain_look'], s) > .55).sum() + (ruido(rng, I['t_look'], s) > .55).sum()) + 2
    d1 = P['d'] + (1-P['d'])*g; d2 = d1 + (1-d1)*.5
    return foco(rng, P, I, s*(1-.5*g)*.5, d2, add, extra_T=n_el*.15 + C_EVAL, tang=True, r=P['r'] + (1-P['r'])*g)

def rodada(seed, fix=None, add=False):
    rng = np.random.default_rng(seed); P = params(rng, **(fix or {}))
    out = {}
    out['V1'] = v1(rng, P, add=add); out['V2'] = v2(rng, P, add=add)
    I = gerar(rng, P, *aloc(30, .4))
    out['V3'] = v3(rng, P, I, add); out['V4'] = v4(rng, P, I, add); out['V5'] = v5(rng, P, I, add)
    out['V4+A'] = v4a(rng, P, I, add)
    I2 = gerar(rng, P, *aloc(45, .4)); out['V4+R'] = v4(rng, P, I2, add)
    out['IDEAL'] = v_ideal(rng, P, I, add)
    for k in out: out[k]['net'] = P['A']*out[k]['Q'] - out[k]['T']
    return P, out

# ---------------------------------------------------------------- experimentos
VAR = ['V1', 'V2', 'V3', 'V4', 'V5', 'V4+A', 'V4+R', 'IDEAL']

def resumo(runs, keys=VAR, sel=None):
    import collections
    R = collections.defaultdict(list); best = collections.Counter(); n = 0
    for P, out in runs:
        if sel and not sel(P): continue
        n += 1
        base = {k: out[k] for k in ['V1', 'V2', 'V3', 'V4', 'V5']}
        best[max(base, key=lambda k: base[k]['net'])] += 1
        for k in keys:
            for m in ['Q', 'T', 'T1', 'rep', 'surp', 'dano', 'comps']: R[(k, m)].append(out[k][m])
    tab = {k: {m: float(np.mean(R[(k, m)])) for m in ['Q', 'T', 'T1', 'rep', 'surp', 'dano', 'comps']} for k in keys}
    for k in ['V1', 'V2', 'V3', 'V4', 'V5']: tab[k]['melhor_%'] = 100*best[k]/max(n, 1)
    return n, tab

def show(title, n, tab):
    print(f"\n== {title} (n={n})")
    print(f"{'var':6} {'Q':>6} {'T1':>6} {'T':>7} {'comps':>6} {'rep':>5} {'surp':>5} {'dano%':>6} {'melhor%':>8}")
    for k, v in tab.items():
        print(f"{k:6} {100*v['Q']:6.1f} {v['T1']:6.1f} {v['T']:7.1f} {v['comps']:6.1f} {v['rep']:5.1f} {v['surp']:5.2f} {100*v['dano']:6.1f} {v.get('melhor_%', float('nan')):8.1f}")

def experimentos_extras():

    def media(fn, n, fix, seed0):
        Q, T1 = [], []
        for i in range(n):
            rng = np.random.default_rng(seed0 + i); P = params(rng, **fix); o = fn(rng, P)
            Q.append(o['Q']); T1.append(o['T1'])
        return 100*np.mean(Q), np.mean(T1)

    print("== C) Fração do esforço em ideias tangenciais (N=30, w=0.4): Q médio")
    shares = [0, .1, .2, .3, .4, .6]
    print("p_s   " + " ".join(f"{s:>6.0%}" for s in shares))
    for ps in [0, .05, .10, .20]:
        row = []
        for s in shares:
            fn = lambda rng, P, s=s: v4(rng, P, gerar(rng, P, *aloc(30, s)))
            row.append(media(fn, 2500, {'w': .4, 'p_s': ps}, 7*10**6)[0])
        print(f"{ps:<5} " + " ".join(f"{q:6.1f}" for q in row))

    print("\n== D) Retornos decrescentes: N ideias (share .4, w=.4)  Q | dias de etapa 1")
    for lab, sig in [('avaliação boa  (σ=.07)', .07), ('avaliação ruim (σ=.25)', .25)]:
        for N in [10, 20, 30, 45, 60, 90]:
            q, t = media(lambda rng, P, N=N: v4(rng, P, gerar(rng, P, *aloc(N, .4))), 2500, {'w': .4, 'sigma': sig}, 8*10**6)
            qa, ta = media(lambda rng, P, N=N: v4a(rng, P, gerar(rng, P, *aloc(N, .4))), 2500, {'w': .4, 'sigma': sig}, 8*10**6)
            print(f"{lab} N={N:<3} V4: Q={q:5.1f} T1={t:5.1f} | V4+A: Q={qa:5.1f} T1={ta:5.1f}")

    print("\n== E) V3 sem dano e sem diluição (só o efeito do CIR amplo no custo)")
    q3 = media(lambda rng, P: v3(rng, P, gerar(rng, P, *aloc(30, .4))), 3000, {'p_h': 0, 'dil': 0}, 9*10**6)
    q4 = media(lambda rng, P: v4(rng, P, gerar(rng, P, *aloc(30, .4))), 3000, {'p_h': 0, 'dil': 0}, 9*10**6)
    T3 = []; T4 = []
    for i in range(3000):
        rng = np.random.default_rng(9*10**6 + i); P = params(rng, p_h=0, dil=0); I = gerar(rng, P, *aloc(30, .4))
        T3.append(v3(rng, P, I)['T']); T4.append(v4(rng, P, I)['T'])
    print(f"V3 Q={q3[0]:.1f} T={np.mean(T3):.1f} | V4 Q={q4[0]:.1f} T={np.mean(T4):.1f}")

    print("\n== F) Combinações e versão leve da sua proposta (todas as premissas aleatórias)")
    def v5a(rng, P, I):
        g = P['g']; P2 = dict(P); P2['sigma'] = P['sigma']*.5; P2['d'] = P['d'] + (1-P['d'])*.5
        return v5(rng, P2, I) | {}
    def v5leve(rng, P, I):
        old = C_ELAB; globals()['C_ELAB'] = .15; P2 = dict(P); P2['g'] = P['g']*.6
        o = v5(rng, P2, I); globals()['C_ELAB'] = old; return o
    for nome, fn, extra in [('V4', v4, 0), ('V4+A', v4a, 0), ('V5 (CIR amplo elaborado)', v5, 0),
                            ('V5 leve (esboço integrado)', v5leve, 0), ('V5+A', v5a, C_EVAL),
                            ('V4+R (45 ideias)', None, 0), ('IDEAL (esboço curto + avaliação forte)', v_ideal, 0)]:
        Q, T1 = [], []
        for i in range(4000):
            rng = np.random.default_rng(10**7 + i); P = params(rng)
            if fn is None:
                o = v4(rng, P, gerar(rng, P, *aloc(45, .4)))
            else:
                I = gerar(rng, P, *aloc(30, .4)); o = fn(rng, P, I)
            Q.append(o['Q']); T1.append(o['T1'] + extra)
        print(f"{nome:28} Q={100*np.mean(Q):5.1f}  dias etapa 1={np.mean(T1):5.1f}")

if __name__ == '__main__':
    NR = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    runs = [rodada(i) for i in range(NR)]
    show('Todas as premissas aleatórias', *resumo(runs))
    for w, nome in [(.05, 'w=0.05 (máquina p/ máquina)'), (.4, 'w=0.4 (apoio à decisão, ex. Motor)'), (.7, 'w=0.7 (hábito/saúde/educação)')]:
        show(nome, *resumo([rodada(10**6 + i, {'w': w}) for i in range(NR//2)]))
    show('Sem ideias anti-ideais (p_h<0.03)', *resumo(runs, sel=lambda P: P['p_h'] < .03))
    show('Forma aditiva (premissa favorável ao foco no núcleo)', *resumo([rodada(2*10**6 + i, add=True) for i in range(NR//2)]))
    # dominância V4 vs V3
    dom = np.mean([o['V4']['Q'] >= o['V3']['Q'] and o['V4']['T'] <= o['V3']['T'] for P, o in runs])
    print(f"\nV4 domina V3 (Q maior E custo menor) em {100*dom:.1f}% das combinações")
    # V1 vs V4 por faixa de w
    for lo, hi in [(0, .1), (.1, .2), (.2, .4), (.4, .8)]:
        sub = [(P, o) for P, o in runs if lo <= P['w'] < hi]
        print(f"w em [{lo},{hi}): V4 > V1 em valor líquido em {100*np.mean([o['V4']['net'] > o['V1']['net'] for P, o in sub]):.0f}%  | ΔQ={100*np.mean([o['V4']['Q']-o['V1']['Q'] for P, o in sub]):+.1f}")
    experimentos_extras()
