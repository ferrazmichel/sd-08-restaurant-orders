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

            if customer in customers_info:
                if meal in customers_info[customer]:
                    customers_info[customer][meal] += 1
                else:
                    customers_info[customer].update({meal: 1})
            else:
                customers_info[customer] = {meal: 1}

            if customer in customer_visits:
                if visit in customer_visits[customer]:
                    customer_visits[customer][visit] += 1
                else:
                    customer_visits[customer].update({visit: 1})
            else:
                customer_visits[customer] = {visit: 1}

    # Create Reports for questions:

    #   Qual o prato mais pedido por 'maria'?
    #   Quantas vezes 'arnaldo' pediu 'hamburguer'?
    #   Quais pratos 'joao' nunca pediu?
    #   Quais dias 'joao' nunca foi na lanchonete?

    # first_answer = ""
    # second_answer = ""
    # third_answer = ""
    # forth_answer = ""

    print(customers_info)
    print(customer_visits)
