import csv
# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/


def analyze_log(path_to_file):
    data, rangos, dias = read_Data(path_to_file)
    item1 = maria_order(data)
    item2 = arnaldo_order(data)
    item3 = joao_no_order(data, rangos)
    item4 = days_of_joao(data, dias)

    print(item1, item2, item3, item4)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{item1}\n"
            f"{item2}\n"
            f"{item3}\n"
            f"{item4}\n"
        )


def read_Data(path_to_file):
    dados = []
    rangos = set()
    dias = set()
    with open(path_to_file) as file:
        data = csv.reader(file)
        for client, rango, day in data:
            dados.append({'client': client, 'rango': rango, 'day': day})
            rangos.add(rango)
            dias.add(day)
    return dados, rangos, dias


def maria_order(data):
    maria = []
    for cada in data:
        if cada['client'] == 'maria':
            maria.append(cada)
    myMax = [d['rango'] for d in maria]
    ops = max(set(myMax), key=myMax.count)
    return ops


def arnaldo_order(data):
    arnaldo = []
    order = []
    for cada in data:
        if cada['client'] == 'arnaldo':
            arnaldo.append(cada)
    # print(arnaldo)
    for each_order in arnaldo:
        if each_order['rango'] == 'hamburguer':
            order.append(each_order['rango'])
    return len(order)


def joao_no_order(data, rangos):
    joao = []
    orders = set()
    for cada in data:
        if cada['client'] == 'joao':
            joao.append(cada)
            orders.add(cada['rango'])
    return rangos.difference(orders)


def days_of_joao(data, dias):
    joao = []
    days_of_joao = set()
    for cada in data:
        if cada['client'] == 'joao':
            joao.append(cada)
            days_of_joao.add(cada['day'])
    # print(days_of_joao)
    return dias.difference(days_of_joao)
