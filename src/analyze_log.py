import csv


def import_data(path):
    """validando o caminho"""
    try:
        list_data = []
        with open(path) as file:
            reader = csv.reader(file, delimiter="\n")
            for elem in reader:
                refact = elem[0].split(",")
                list_data.append(refact)
            return list_data
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def food_favorite_maria(data_orders):
    """Função que responde a primeira pergunta verificando a comida
    favorita 'elem[1]' de Maria
    """
    orders = []
    conjunct_count = set()
    for elem in data_orders:
        if elem[0] == "maria":
            orders.append(elem[1])
    for order in orders:
        conjunct_count.add((orders.count(order), order))
        dict_count = dict(conjunct_count)
    return dict_count[max(dict_count)]


def hamburguer_request_by_arnaldo(data_orders):
    """Função que responde a segunda pergunta
    retornando quantos hamburguers o Arnaldo pediu através do count
    """
    orders = []
    for elem in data_orders:
        if elem[0] == "arnaldo":
            orders.append(elem[1])
    return orders.count("hamburguer")


def never_asked_joao(data_orders):
    """Função que responde a terceira pergunta
    encontrando a diferença entre os set's
    """
    joao_order = set()
    not_joao_orders = set()
    for elem in data_orders:
        if elem[0] == "joao":
            joao_order.add(elem[1])
        else:
            not_joao_orders.add(elem[1])
    return not_joao_orders - joao_order


def joao_never_visited(data_days):
    """Função que responde a última pergunta
    encontrando a diferença entre os set's
    """
    joao_days = set()
    days = set()
    for elem in data_days:
        if elem[0] == "joao":
            joao_days.add(elem[2])
        else:
            days.add(elem[2])
    return days - joao_days


def analyze_log(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")

    data = import_data(path)
    maria_requests = food_favorite_maria(data)
    arnaldo_requests = hamburguer_request_by_arnaldo(data)
    joao_requests = never_asked_joao(data)
    visited = joao_never_visited(data)

    txt = open("data/mkt_campaign.txt", "w")
    txt.write(
        f"{maria_requests}\n{arnaldo_requests}\n{joao_requests}\n{visited}"
    )
    txt.close()
    return True
