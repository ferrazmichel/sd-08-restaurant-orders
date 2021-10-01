import csv


def analyze_log(path_to_file):
    restaurant_menu = set()
    restaurant_dates = set()
    customers_info = dict()
    customer_visits = dict()

    # Data Treatment
    with open(path_to_file, "r") as file:
        file_reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in file_reader:
            customer = row[0]
            meal = row[1]
            visit = row[2]

            restaurant_menu.add(meal)
            restaurant_dates.add(visit)
            if customer not in customers_info:
                customers_info[customer] = []
            if customer not in customer_visits:
                customer_visits[customer] = []

            customers_info[customer].append(meal)
            customer_visits[customer].append(visit)

    # Create Reports for questions:

    #   Qual o prato mais pedido por 'maria'?
    #   Quantas vezes 'arnaldo' pediu 'hamburguer'?
    #   Quais pratos 'joao' nunca pediu?
    #   Quais dias 'joao' nunca foi na lanchonete?

    maria_meals = customers_info["maria"]
    first_answer = max(set(maria_meals), key=maria_meals.count)

    second_answer = customers_info["arnaldo"].count("hamburguer")

    third_answer = restaurant_menu - set(customers_info["joao"])

    forth_answer = restaurant_dates - set(customer_visits["joao"])

    with open("data/mkt_campaign.txt", mode="w") as file_object:
        file_object.write(first_answer + "\n")
        file_object.write(str(second_answer) + "\n")
        file_object.write(str(third_answer) + "\n")
        file_object.write(str(forth_answer))
