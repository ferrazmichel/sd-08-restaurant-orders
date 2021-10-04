import csv


class plate:

    @staticmethod
    def repeated(name, plate, orders):
        client_order = set()
        for order in orders:
            if order[0] == name and order[1] == plate:
                client_order.add(order[1])
        return len(client_order)

    @staticmethod
    def favorite(name, orders):
        count = dict()
        max_order = 0
        favorite = ""
        for order in orders:
            if order[0] == name:
                if order[1] in count:
                    count[order[1]] += 1
                else:
                    count[order[1]] = 1
                if count[order[1]] > max_order:
                    max_order = count[order[1]]
                    favorite = order[1]
        return favorite

    @staticmethod
    def never_ordered(name, orders):
        order_client = set()
        all_orders = set()
        for order in orders:
            all_orders.add(order[1])
        for order in orders:
            if order[0] == name:
                order_client.add(order[1])
        return all_orders.difference(order_client)

    @staticmethod
    def days_without_orders(name, orders):
        days_with_orders = set()
        all_days = set()
        for order in orders:
            all_days.add(order[2])
        for order in orders:
            if order[0] == name:
                days_with_orders.add(order[2])
        return all_days.difference(days_with_orders)


def analyze_log(path_to_file):
    if path_to_file.split('.')[1] != 'csv':
        path_to_file_txt = path_to_file.replace("'", "") + "'"
        eror_msg = "No such file or directory: '" + path_to_file_txt
        raise FileNotFoundError(eror_msg)

    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",")
        orders = list(data)

    with open("data/mkt_campaign.txt", "w") as analyze_file:
        analyze_file.write(f"{plate.favorite('maria', orders)}\n")
        analyze_file.write(
            f"{plate.repeated('arnaldo','hamburguer', orders)}\n"
        )
        analyze_file.write(
            f"{plate.never_ordered('joao', orders)}\n"
        )
        analyze_file.write(f"{plate.days_without_orders('joao', orders)}\n")
