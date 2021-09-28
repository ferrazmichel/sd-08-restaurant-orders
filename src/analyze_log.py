import csv
from types import FunctionType
from typing import Iterable

fieldnames = ["nome", "prato", "dia"]

analyze_value = {
    "maria": {},
    "arnaldo": 0,
    "joao_pratos": set(),
    "joao_dias": set(),
    "dias": set(),
    "pratos": set(),
}


def pratos_maria(value_maria, value):
    if value_maria.get(value["prato"]):
        value_maria[value["prato"]] += 1
    else:
        value_maria[value["prato"]] = 1

    return value_maria


def arnaldo_get_hamburguer(value_arnaldo, value):
    if value["prato"] == "hamburguer":
        value_arnaldo += 1

    return value_arnaldo


def joao_pratos_dias(joao_pratos, joao_dias, value):
    joao_pratos.add(value["prato"])
    joao_dias.add(value["dia"])
    return joao_pratos, joao_dias


def reducer_log(ac, value, _, __):
    if value["nome"] == "maria":
        ac["maria"] = pratos_maria(ac["maria"], value)

    if value["nome"] == "arnaldo":
        ac["arnaldo"] = arnaldo_get_hamburguer(ac["arnaldo"], value)

    if value["nome"] == "joao":
        ac["joao_pratos"], ac["joao_dias"] = joao_pratos_dias(
            ac["joao_pratos"], ac["joao_dias"], value
        )

    ac["dias"].add(value["dia"])
    ac["pratos"].add(value["prato"])

    return ac


def my_reducer(this: Iterable, func_reduce: FunctionType, ac: list = []):
    for key, value in enumerate(this):
        ac = func_reduce(ac, value, key, this)

    return ac


def analyze_log(path_to_file):
    list_file = list()
    list_result = []
    path_file = "data/mkt_campaign.txt"

    with open(path_to_file) as file:
        list_file = list(
            csv.DictReader(
                file, delimiter=",", quotechar='"', fieldnames=fieldnames
            )
        )

    result = my_reducer(list_file, reducer_log, analyze_value)

    mais_pedido_maria = max(result["maria"].items(), key=lambda x: x[1])
    list_result.append(mais_pedido_maria[0])

    list_result.append(result["arnaldo"])

    joao_nunca_pediu = result["pratos"] - result["joao_pratos"]
    list_result.append(joao_nunca_pediu)

    dias_joao_nunca_foi_lanchonete = result["dias"] - result["joao_dias"]
    list_result.append(dias_joao_nunca_foi_lanchonete)

    with open(path_file, "w") as file:
        [file.write(f"{x}\n") for x in list_result]
