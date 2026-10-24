#!/usr/bin/env python3
"""Projeta itens para cobertura.py sem inventar especialidades nem confundir lacunas com jobs."""
import argparse
from mapa import validate
from mapa_core import cli, dump, load


def inventory(value):
    validate(value)
    items = []
    for kind, field in [("job", "etapas"), ("causa", "falhas"), ("causa", "causas"), ("contradicao", "contradicoes"), ("parte", "partes")]:
        for obj in value[field]:
            if field == "falhas" and not obj["central"]:
                continue
            items.append({"id": obj["id"], "tipo": kind,
                          "texto": obj.get("texto") or " × ".join(obj["parametros"]),
                          "central": obj.get("central", False) or (field == "causas" and any(f["id"] == obj["falha"] and f["central"] for f in value["falhas"])),
                          "principio": obj.get("classe") == "principio"})
    # O schema atual da especialistas não admite tipo 'lacuna'. Não o alteramos silenciosamente.
    gaps = [{"id": k["id"], "texto": k["texto"], "resolveria": k["resolveria"]}
            for k in value["conhecimento"] if k["classe"] == "incerto"]
    return {"schema_version": 1, "itens": items, "especialidades": [], "temas": [],
            "lacunas_espaco_k": gaps,
            "limite": "Falha central usa tipo causa com ID próprio. Lacunas ficam separadas: ligar aos itens do problema antes de cobertura; não são cobertura verificada."}


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("entrada")
    a = p.parse_args(); print(dump(inventory(load(a.entrada))), end="")


if __name__ == "__main__":
    raise SystemExit(cli(main))
