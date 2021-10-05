import csv


def read_csv(path_to_file):
    with open(path_to_file, "r") as file:
        return list(csv.reader(file))


def dish_most_ordered(orders, client):
    orders_counter = {}

    for order in orders:
        if order[0] == client:
            if order[1] not in orders_counter:
                orders_counter[order[1]] = 1
            else:
                orders_counter[order[1]] += 1

    result = max(orders_counter, key=orders_counter.get)

    return result


def total_orders(orders, client, dish):
    count = 0

    for item in orders:
        if item[0] == client and item[1] == dish:
            count += 1

    return count


def dish_not_ordered(orders, client):
    all_recipes = set()
    recipe_client = set()

    for item in orders:
        all_recipes.add(item[1])

        if item[0] == client:
            recipe_client.add(item[1])

    result = all_recipes - recipe_client

    return result


def days_without_client(orders, client):
    all_days = set()
    client_day = set()

    for item in orders:
        all_days.add(item[2])

        if item[0] == client:
            client_day.add(item[2])

    result = all_days - client_day

    return result


def analyze_log(path_to_file):
    '''
    Escreva uma função que responda às seguintes perguntas abaixo:
    - Qual o prato mais pedido por 'maria'? R- hamburguer
    - Quantas vezes 'arnaldo' pediu 'hamburguer'? R- 1
    - Quais pratos 'joao' nunca pediu? R- {'pizza', 'coxinha', 'misto-quente'}
    - Quais dias 'joao' nunca foi na lanchonete? R- {'sabado', 'segunda-feira'}

    A função não retornará nada! A função deve apenas salvar as respostas no
    arquivo `data/mkt_campaign.txt`, na mesma ordem que acima.
    '''
    result = ''

    data = read_csv(path_to_file)

    maria_dish_most_ordered = dish_most_ordered(data, "maria")
    arnaldo_total_orders = total_orders(data, "arnaldo", "hamburguer")
    joao_dish_not_ordered = dish_not_ordered(data, "joao")
    joao_days_without_client = days_without_client(data, "joao")

    result = (
        f"{maria_dish_most_ordered}\n"
        f"{arnaldo_total_orders}\n"
        f"{joao_dish_not_ordered}\n"
        f"{joao_days_without_client}\n"
    )

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(result)
