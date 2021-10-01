import csv


def more_request_by_Maria(orders_list):
    count = {}
    most_frequent = orders_list[0]["Comida"]

    for order in orders_list:
        name, food = (order["Nome"], order["Comida"])
        if name == "maria":
            if food not in count:
                count[food] = 1
            else:
                count[food] += 1
                if count[food] > count[most_frequent]:
                    most_frequent = food
    return most_frequent


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        orders_reader = csv.reader(file, delimiter=",")
        orders_list = [{"Nome": row[0], "Comida": row[1], "dia": row[2]}
                       for row in orders_reader]
    return more_request_by_Maria(orders_list)


print(analyze_log("data/orders_1.csv"))
