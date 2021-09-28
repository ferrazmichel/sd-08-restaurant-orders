import csv
import operator


def analyze_log(path_to_file):
    food_maria = []
    food_arnaldo = 0
    total_foods = set()
    foods_joao = set()
    total_days = set()
    days_joao = set()
    with open(path_to_file) as file:
        content = csv.reader(file)
        for line in content:
            total_foods.add(line[1])
            total_days.add(line[2])
            if line[0] == "maria":
                food_maria.append(line[1])
            if line[0] == "arnaldo" and line[1] == "hamburguer":
                food_arnaldo += 1
            if line[0] == "joao":
                foods_joao.add(line[1])
                days_joao.add(line[2])
    values_maria = get_repeated(food_maria)
    # https://www.delftstack.com/pt/howto/python/find-max-value-in-dictionary-python/
    max_key = max(values_maria.items(), key=operator.itemgetter(1))[0]

    never_order_joao = total_foods.difference(foods_joao)

    never_been_joao = total_days.difference(days_joao)

    # print(max_key)
    # print(food_arnaldo)
    # print(never_order_joao)
    # print(never_been_joao)

    # cria data/mkt_campaign.txt
    json_string = (
        f"{max_key}\n{food_arnaldo}\n{never_order_joao}\n{never_been_joao}\n"
    )

    txt_file = open("data/mkt_campaign.txt", "w")
    txt_file.write(json_string)
    txt_file.close()


def get_repeated(values):
    # Lógica retirada do Bloco 37 - Sets
    seen_before = set()
    repeated = set()

    result_maria = {}

    for value in values:
        if value in seen_before:
            repeated.add(value)
        else:
            seen_before.add(value)

    for element in repeated:
        result_maria[element] = values.count(element)

    return result_maria
