from collections import Counter
import csv


def count_ordered_product(results, client, product):
    """ Count ordered products by client """
    products = list((
        record['product'] for record in results
        if record['client'] == client
        and record['product'] == product
    ))
    return products.count(product)


def count_never_ordered(results, client):
    """ Count never ordered products by client """
    products = set((record['product'] for record in results))
    products_by_client = set((
        record['product'] for record in results
        if record['client'] == client
    ))
    return products.difference(products_by_client)


def get_most_ordered(results, client):
    """ Returns most ordered product by client """
    products = list((
        record['product'] for record in results
        if record['client'] == client
    ))
    return Counter(products).most_common()[0][0]


def get_not_visited_days(results, client):
    """ List never visited days by client """
    days = set((record['day'] for record in results))
    visited_days = set((
        record['day'] for record in results
        if record['client'] == client
    ))
    return days.difference(visited_days)


def read_content(file):
    """ Given a csv file name, reads it and return its content """
    try:
        with open(file) as csvfile:
            content = csv.DictReader(
                csvfile,
                fieldnames=['client', 'product', 'day']
            )
            results = list(row for row in content)
            return results
    except ValueError:
        raise FileNotFoundError(f"No such file or directory: '{file}'")


def write_content(new_file, report):
    """ Given a new file name, writes its content to disk """
    with open(new_file, 'w') as file:
        file.writelines(report)


def analyze_log(path_to_file):
    file = read_content(path_to_file)
    report = [
        f"{get_most_ordered(file, 'maria')}\n",
        f"{count_ordered_product(file, 'arnaldo', 'hamburguer')}\n",
        f"{count_never_ordered(file, 'joao')}\n",
        f"{get_not_visited_days(file, 'joao')}\n"
    ]
    write_content("data/mkt_campaign.txt", report)
