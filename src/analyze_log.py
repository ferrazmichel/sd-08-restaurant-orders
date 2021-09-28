import csv


def get_all_orders(path_to_file):
    with open(path_to_file) as f:
        reader = csv.reader(f)
        person_dict = dict()
        food = set()
        day = set()

        for row in reader:
            food.add(row[1])
            day.add(row[2])
            if row[0] in person_dict:
                # append the new number to the existing array at this slot
                person_dict[row[0]].append((row[1], row[2]))
            else:
                # create a new array in this slot
                person_dict[row[0]] = [(row[1], row[2])]
    return person_dict, food, day


def analyze_log(path_to_file):
    person_dict, food, day = get_all_orders(path_to_file)
    maria_eats = []
    for row in person_dict["maria"]:
        maria_eats.append(row[0])
    maria_dict = {i: maria_eats.count(i) for i in maria_eats}
    maria_result = max(maria_dict, key=maria_dict.get)
    print(maria_result)

    arnaldo_result = 0
    for row in person_dict["arnaldo"]:
        if row[0] == "hamburguer":
            arnaldo_result += 1

    joao_foodoff = set()
    joao_dayoff = set()
    for row in person_dict["joao"]:
        joao_foodoff.add(row[0])
        joao_dayoff.add(row[1])

    joao_result_food = food.difference(joao_foodoff)
    joao_result_day = day.difference(joao_dayoff)

    with open("data/mkt_campaign.txt", mode="w") as f:
        f.write(
            f"{str(maria_result)}\n{str(arnaldo_result)}\n"
            f"{str(joao_result_food)}\n{str(joao_result_day)}"
        )
