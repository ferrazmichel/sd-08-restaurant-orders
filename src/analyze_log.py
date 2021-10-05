import csv
from statistics import mode
# https://www.geeksforgeeks.org/python-statistics-mode-function/
# http://www.bosontreinamentos.com.br/programacao-em-python/como-gravar-dados-em-arquivos-de-texto-com-python/


def analyze_log(path_to_file):
    joao_ord = set()
    joao_days = set()
    days = set()
    meals = set()
    maria_ord = []
    count = 0

    with open(path_to_file) as file_content:
        data_values = csv.reader(file_content)

        for order in data_values:
            meals.add(order[1])
            days.add(order[2])
            if order[0] == "maria":
                maria_ord.append(order[1])
            if order[0] == "joao":
                joao_ord.add(order[1])
                joao_days.add(order[2])
            if order[0] == "arnaldo" and order[1] == "hamburguer":
                count += 1

    write_to_file = open('data'+'/'+'mkt_campaign.txt', 'w')

    write_to_file.write(f"{mode(maria_ord)}\n")
    write_to_file.write(f"{count}\n")
    write_to_file.write(f"{meals - joao_ord}\n")
    write_to_file.write(f"{days - joao_days}\n")
