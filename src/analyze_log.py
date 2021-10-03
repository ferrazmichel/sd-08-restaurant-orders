import csv


def generate_answers(rest_menu, rest_days, orders, visits):
    # Create Reports for questions:
    #   Qual o prato mais pedido por 'maria'?
    #   Quantas vezes 'arnaldo' pediu 'hamburguer'?
    #   Quais pratos 'joao' nunca pediu?
    #   Quais dias 'joao' nunca foi na lanchonete?

    first_answer = max(set(orders["maria"]), key=orders["maria"].count)

    second_answer = orders["arnaldo"].count("hamburguer")

    third_answer = rest_menu - set(orders["joao"])

    forth_answer = rest_days - set(visits["joao"])

    with open("data/mkt_campaign.txt", mode="w") as file_object:
        file_object.write(first_answer + "\n")
        file_object.write(str(second_answer) + "\n")
        file_object.write(str(third_answer) + "\n")
        file_object.write(str(forth_answer))


def analyze_log(path_to_file):
    restaurant_menu = set()
    restaurant_dates = set()
    customers_orders = dict()
    customers_visits = dict()

    # Data Treatment
    with open(path_to_file, "r") as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in file_reader:
            customer = row[0]
            meal = row[1]
            visit = row[2]

            # set restaurant menu and dates
            restaurant_menu.add(meal)
            restaurant_dates.add(visit)

            # set new customer
            if customer not in customers_orders:
                customers_orders[customer] = []
            if customer not in customers_visits:
                customers_visits[customer] = []

            # add customers order and date of visit
            customers_orders[customer].append(meal)
            customers_visits[customer].append(visit)

    generate_answers(
        restaurant_menu, restaurant_dates, customers_orders, customers_visits
        )
