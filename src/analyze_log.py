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


def dishes_never_ordered(name, orders):
    client_order = set()
    all_orders = set()
    for order_row in orders:
        all_orders.add(order_row[1])
    for client_row in orders:
        if client_row[0] == name:
            client_order.add(client_row[1])
    return all_orders.difference(client_order)


def analyze_log(path_to_file):
    raise NotImplementedError
