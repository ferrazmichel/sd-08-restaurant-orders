def favorite_dish(name, orders):
    favorite_dish = ""
    for row in orders:
        if row[0] == name:
            favorite_dish = row[1]
            break
    return favorite_dish


def repeated_dishes(name, dish, orders):
    client_order = set()
    for row in orders:
        if row[0] == name and row[1] == dish:
            client_order.add(row[1])
    return len(client_order)





def analyze_log(path_to_file):
    raise NotImplementedError
