# 1- Finding difference between lists (Mohideen bin Mohammed answer):
# https://stackoverflow.com/questions/3462143/get-difference-between-two-lists

import os.path as check
from .importer.csv_importer import CsvImporter
import src.order_filters as f


def analyze_log(path_to_file):
    if (not check.isfile(path_to_file) or path_to_file[-3:] != "csv"):
        raise FileNotFoundError(
            "No such file or directory: " "'{}'".format(path_to_file)
        )
    all_orders = CsvImporter.import_data('data/orders_1.csv')

    maria_orders = f.filter_by_client(all_orders, 'maria')
    maria_most_ordered = f.find_most_repeated_value(maria_orders, 'order')
    # print('OK_MARIA_MOST_ORDERED', maria_most_ordered)

    arnaldo_orders = f.filter_by_client(all_orders, 'arnaldo')
    arnaldo_hamburguers_count = len(
        f.filter_by_order(arnaldo_orders, 'hamburguer')
    )
    # print('OK_ARNALDO_HAMBURGUERS', arnaldo_hamburguers_count)
    # print(all_orders)

    all_dishes = f.get_values_from_field(all_orders, 'order')
    joao_orders = f.filter_by_client(all_orders, 'joao')
    joao_dishes = f.get_values_from_field(joao_orders, 'order')
    joao_didnt_order = list(set(all_dishes).difference(set(joao_dishes)))  # 1
    # print('OK_JOAO_DIDNT_ORDER', set(joao_didnt_order))

    days_joao_did_go = f.get_values_from_field(joao_orders, 'day')
    week_days = f.get_values_from_field(all_orders, 'day')
    days_joao_didnt_go = list(set(week_days).difference(set(days_joao_did_go)))
    # print('OK_JOAO_DIDNT_GO', set(days_joao_didnt_go))

    mkt_string = f"""{maria_most_ordered}
{arnaldo_hamburguers_count}
{set(joao_didnt_order)}
{set(days_joao_didnt_go)}"""
    # print(mkt_string)
    create_file_and_write(mkt_string, 'data/mkt_campaign.txt')


def create_file_and_write(string, path):
    with open(path, "w") as f:
        f.write(string)
