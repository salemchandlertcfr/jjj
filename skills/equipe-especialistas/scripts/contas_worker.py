"""Subconjunto matemático de Python: AST interpretada, sem exec/eval, arquivos ou imports reais."""
import ast
import json
import math
import sys

FUNCTIONS={k:getattr(math,k) for k in ("ceil","floor","log","log10","sqrt","exp","sin","cos")}
FUNCTIONS.update(abs=abs,min=min,max=max,round=round)


def calculate(code):
    if not isinstance(code,str) or len(code)>6000:raise ValueError()
    tree=ast.parse(code)
    if len(list(ast.walk(tree)))>300:raise ValueError()
    names={"pi":math.pi,"e":math.e}
    count=0
    def expr(n):
        nonlocal count
        count+=1
        if count>600:raise ValueError()
        if isinstance(n,ast.Constant) and type(n.value) in {int,float}:v=n.value
        elif isinstance(n,ast.Name) and n.id in names:v=names[n.id]
        elif isinstance(n,ast.UnaryOp) and isinstance(n.op,(ast.UAdd,ast.USub)):
            v=expr(n.operand)*(1 if isinstance(n.op,ast.UAdd) else -1)
        elif isinstance(n,ast.BinOp):
            a,b=expr(n.left),expr(n.right)
            if isinstance(n.op,ast.Add):v=a+b
            elif isinstance(n.op,ast.Sub):v=a-b
            elif isinstance(n.op,ast.Mult):v=a*b
            elif isinstance(n.op,ast.Div):v=a/b
            elif isinstance(n.op,ast.Pow) and abs(b)<=1000:v=a**b
            else:raise ValueError()
        elif isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in FUNCTIONS and not n.keywords and 1<=len(n.args)<=4:
            v=FUNCTIONS[n.func.id](*[expr(a) for a in n.args])
        else:raise ValueError()
        if type(v) not in {int,float} or not math.isfinite(v) or abs(v)>1e100:raise ValueError()
        return v
    result=None
    for statement in tree.body:
        if isinstance(statement,ast.ImportFrom) and statement.module=="math" and statement.level==0:
            if not all(a.name in FUNCTIONS and a.asname is None for a in statement.names):raise ValueError()
        elif isinstance(statement,ast.Assign) and len(statement.targets)==1 and isinstance(statement.targets[0],ast.Name):
            key=statement.targets[0].id
            if key in FUNCTIONS or key.startswith("_"):raise ValueError()
            names[key]=expr(statement.value)
        elif isinstance(statement,ast.Expr) and isinstance(statement.value,ast.Call) and isinstance(statement.value.func,ast.Name) and statement.value.func.id=="print" and len(statement.value.args)==1 and not statement.value.keywords:
            if result is not None:raise ValueError()
            result=expr(statement.value.args[0])
        else:raise ValueError()
    if result is None:raise ValueError()
    return result


if __name__=="__main__":
    try:
        data=json.loads(sys.stdin.read(10000));print(json.dumps({"resultado":calculate(data["codigo"])}))
    except Exception:
        raise SystemExit(1)
