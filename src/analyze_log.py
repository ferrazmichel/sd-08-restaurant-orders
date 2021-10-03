import csv
from collections import Counter


def analyze_log(path_to_file):
    maria_lanches = []
    count = 0
    all_food = set()
    orders_joao = set()
    date = set()
    data_joao = set()
    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",", quotechar='"')
        header, *body = data

        for order in body:
            all_food.add(order[1])
            date.add(order[2])
            if order[0] == 'maria':
                maria_lanches.append(order[1])
            elif order[0] == 'arnaldo' and order[1] == 'hamburguer':
                count += 1
            elif order[0] == 'joao':
                orders_joao.add(order[1])
                data_joao.add(order[2])

    arquive = open('data'+'/'+'mkt_campaign.txt', 'w')
    # https://www.delftstack.com/pt/howto/python/find-max-value-in-dictionary-python/#:~:text=Copy%20key3-,Utilize%20max()%20e%20dict.,%C3%A9%20utilizado%20o%20m%C3%A9todo%20dict.
    # Obter o maior valor de um dicionario
    arquive.write(
        f"{max(Counter(maria_lanches),key=Counter(maria_lanches).get)}\n"
    )
    arquive.write(f"{str(count)}\n")
    arquive.write(f"{str(all_food - orders_joao)}\n")
    arquive.write(f"{str(date - data_joao)}\n")


analyze_log("./data/orders_1.csv")
