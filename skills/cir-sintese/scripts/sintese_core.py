"""Leitura explícita e projeções locais. Nenhuma escrita, agente ou pesquisa implícita."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import unicodedata

TITLES=['Essência em uma frase','Propósito, job e estado ideal','Fenômeno e contradições','Métricas e RFI','Limites','Famílias exploradas','Princípios invariantes','Capacidades','Restrições anti-ideais','Funcionamento','Diferenciais, como hipóteses com confiança','Casos canônicos','Pré-mortem','O que este conceito não é','Passagem à Etapa 2','Estacionamento Etapa 3','Decisões e taxa de surpresa']
TYPES={'proposito','descartada','valor','linha_vermelha','metrica','rfi','limite','fronteira','restricao','principio','capacidade','cenario','caso','saida_ideal','falha_real','ataque','confianca','killer','motivo','dissenso','familia','tangente','pergunta','alternativa_viva','refutada','estacionamento','temor','registro','nucleo'}
SHA=re.compile(r'[0-9a-f]{64}')
COMMIT=re.compile(r'[0-9a-f]{40}')

class Invalid(ValueError):pass

def require(ok,message):
    if not ok:raise Invalid(message)

def text(v,name='Texto'):
    require(isinstance(v,str) and v.strip(),name+' obrigatório');return v

def ident(v):
    require(isinstance(v,str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,99}',v) and v not in {'.','..'},'ID inválido');return v

def array(v):require(isinstance(v,list),'Lista obrigatória');return v

def index(v):
    out={}
    for item in array(v):
        require(isinstance(item,dict),'Objeto obrigatório');k=ident(item.get('id'));require(k not in out,'ID duplicado');out[k]=item
    return out

def refs(v,known=None):
    a=array(v)
    for k in a:ident(k)
    require(len(a)==len(set(a)),'Referência duplicada')
    if known is not None:require(set(a)<=set(known),'Origem desconhecida')
    return a

def dump(v):return json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
def hash_bytes(v):return hashlib.sha256(v).hexdigest()
def digest(v):return hash_bytes(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
def fold(v):return ''.join(c for c in unicodedata.normalize('NFD',v.lower()) if unicodedata.category(c)!='Mn')
def loads(raw):
    if not raw.lstrip().startswith('{'):
        blocks=re.findall(r'^```json cir-sintese-v1\s*\n(.*?)^```\s*$',raw,re.M|re.S)
        require(len(blocks)==1,'Markdown exige uma projeção json cir-sintese-v1');raw=blocks[0]
    def pairs(items):
        d={}
        for k,v in items:require(k not in d,'Chave JSON duplicada');d[k]=v
        return d
    def bad(_):raise Invalid('Número JSON não finito')
    v=json.loads(raw,object_pairs_hook=pairs,parse_constant=bad)
    require(isinstance(v,dict) and type(v.get('schema_version')) is int and v['schema_version']==1,'schema_version 1 obrigatório');return v

def safe(path):
    p=Path(path).absolute();require(not any(x.is_symlink() for x in [p,*p.parents]),'Link simbólico não permitido');return p

def load(path):
    p=safe(path);require(p.stat().st_size<=8_000_000,'Entrada maior que 8 MB');return loads(p.read_text())

def relative(name):
    text(name);p=PurePosixPath(name)
    require(not p.is_absolute() and '..' not in p.parts and str(p)==name and not name.startswith('-') and ':' not in name,'Caminho relativo inválido');return name

def file_at(root,name):
    relative(name);p=safe(Path(root)/name);require(p.is_relative_to(safe(root)),'Caminho fora da raiz');return p

def git(root,*args):
    r=subprocess.run(['git','-C',str(safe(root)),*args],capture_output=True,timeout=15)
    require(r.returncode==0,'Objeto Git indisponível');return r.stdout

def read_ref(root,ref):
    require(COMMIT.fullmatch(text(ref.get('commit'))),'Commit completo obrigatório')
    require(SHA.fullmatch(text(ref.get('sha256'))),'Hash completo obrigatório');name=relative(ref.get('arquivo'))
    tree=git(root,'ls-tree',ref['commit'],'--',name).decode()
    require(tree.startswith('100644 blob ') or tree.startswith('100755 blob '),'Origem deve ser arquivo Git regular')
    raw=git(root,'show',ref['commit']+':'+name)
    require(hash_bytes(raw)==ref['sha256'],'Hash de origem Git divergente')
    return raw

def item_at(root,ref):
    doc=loads(read_ref(root,ref).decode());items=index(doc.get('itens'));k=ident(ref.get('item'));require(k in items,'Item não existe na origem');item=items[k]
    text(item.get('texto'));require(item.get('tipo') in TYPES,'Tipo de item desconhecido')
    require(type(item.get('tema')) is int and 0<=item['tema']<=6,'Tema inválido');text(item.get('subetapa'));ident(item.get('registro'))
    require(isinstance(item.get('dados',{}),dict),'Dados devem ser objeto');return item

def context(manifest,root):
    require(COMMIT.fullmatch(text(manifest.get('commit_base'))),'Commit base completo obrigatório')
    git(root,'cat-file','-e',manifest['commit_base']+'^{commit}')
    expected=manifest.get('hashes_estado');require(isinstance(expected,dict) and bool(expected),'Hashes do estado obrigatórios')
    registered={}
    for name,h in expected.items():
        require(isinstance(h,str) and SHA.fullmatch(h),'Hash do estado inválido')
        raw=file_at(root,name).read_bytes();require(hash_bytes(raw)==h,'Origem mudou sem registro: '+name)
        require(hash_bytes(git(root,'show',manifest['commit_base']+':'+relative(name)))==h,'Estado não corresponde ao commit base')
        # Inventário deriva dos registros completos, não da lista de blocos.
        source_items=index(loads(raw.decode()).get('itens'))
        require(not set(registered)&set(source_items),'ID repetido entre registros de origem')
        registered.update(source_items)
    result={};catalog={}
    for slot in ('inventario','blocos'):
        out={}
        for k,b in index(manifest.get(slot)).items():
            ref=b.get('origem',{});require(ref.get('arquivo') in expected,'Origem ausente dos hashes do estado')
            require(ref.get('sha256')==expected[ref['arquivo']],'Bloco superado sem atualização de origem')
            require(git(root,'merge-base','--is-ancestor',ref['commit'],manifest['commit_base'])==b'','Origem fora da ancestralidade')
            item=item_at(root,ref);require(item['id']==k,'ID do bloco diverge da origem')
            if slot=='blocos':require(type(b.get('secao')) is int and 1<=b['secao']<=17,'Seção inválida')
            out[k]={'bloco':b,'item':item}
        if slot=='inventario':catalog=out
        else:result=out
    require(set(catalog)==set(registered),'Inventário omite ou inventa item dos registros completos')
    if manifest.get('suas_versoes'):
        require(any(i.get('tipo')=='temor' and i.get('texto')==manifest['suas_versoes'].get('temor') for i in registered.values()),'Temor da abertura ausente da cobertura')
    for k,v in result.items():require(k in catalog and v['item']==catalog[k]['item'],'Bloco não consta no inventário independente')
    require(manifest.get('escolha') in {'referencia','refutada','abstencao'},'Declare escolha do tema 5')
    return result,catalog

def section(v,manifest):
    b,item=v['bloco'],v['item']
    if b.get('superado_por'):return 17
    if item['tipo']=='dissenso':return 17
    if item.get('dados',{}).get('familia_perdeu') and 7<=b['secao']<=10:return 6
    return b['secao']

def signals(body):
    normalized=fold(body);out=[]
    patterns={'generalizacao':r'\b(sempre|todas|todos|nunca|garante|garantem)\b',
              'meio':r'\b(tela|tecnologia|aplicativo|software|sensor|sensores|plataforma|marca|produto)\b',
              'mercado':r'\b(preco|canal|mercado|venda|receita)\b'}
    for kind,pattern in patterns.items():
        for m in re.finditer(pattern,normalized):out.append({'tipo':kind,'inicio':m.start(),'sinal':m.group()})
    return out

def evidence(root,e,item_id):
    raw=read_ref(root,e);require(hash_bytes(file_at(root,e['arquivo']).read_bytes())==e['sha256'],'Evidência de outra versão')
    doc=loads(raw.decode());items=index(doc.get('evidencias'));require(item_id in items,'Evidência ausente')
    item=items[item_id];require(item.get('item')==e.get('criterio'),'Evidência de outro critério')
    require(text(e.get('secao'))==item.get('secao'),'Seção da evidência divergente');return item

def cli(main):
    try:return main() or 0
    except (Invalid,OSError,ValueError,KeyError,TypeError,subprocess.SubprocessError) as exc:
        print('ERRO: '+str(exc),file=sys.stderr);return 1
