def person_orders(person_list):
    food_amount = {}

    for food in person_list:
        try:
            food_amount[food["order"]] += 1
        except KeyError:
            food_amount[food["order"]] = 1

    return food_amount


def person_dates(person_list):
    date_amount = {}

    for date in person_list:
        try:
            date_amount[date["day"]] += 1
        except KeyError:
            date_amount[date["day"]] = 1

    return date_amount


def never_ordered_joao(joao, available_order):
    not_ordered = []
    joao_foods = person_orders(joao)
    for order in available_order:
        try:
            bool(joao_foods[order])
        except KeyError:
            not_ordered.append(order)
    return set(not_ordered)


def never_frequented_joao(joao):
    days = [
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sabado",
        "domingo",
    ]
    not_frequented = []
    joao_dates = person_dates(joao)

    for day in days:
        try:
            bool(joao_dates[day])
        except KeyError:
            not_frequented.append(day)
    return set(not_frequented)


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        orders_by_person = {}
        available_orders = []
        lines = file.readlines()
        for line in lines:
            [name, order, day] = line.rstrip().split(",")
            available_orders.append(order)
            try:
                orders_by_person[name].append({"order": order, "day": day})
            except KeyError:
                orders_by_person[name] = [{"order": order, "day": day}]
        available_orders = set(available_orders)
        maria_orders = person_orders(orders_by_person["maria"])
        maria_answer = max(maria_orders, key=maria_orders.get)

        arnaldo_orders = person_orders(orders_by_person["arnaldo"])
        arnaldo_answer = arnaldo_orders["hamburguer"]

        joao_order_answer = never_ordered_joao(
            orders_by_person["joao"], available_orders)
        joao_day_answer = never_frequented_joao(orders_by_person["joao"])

        result = open('data/mkt_campaign.txt', 'w')
        result.write(
            f"{maria_answer}\n"
            f"{arnaldo_answer}\n"
            f"{joao_order_answer}\n"
            f"{joao_day_answer}"
        )
