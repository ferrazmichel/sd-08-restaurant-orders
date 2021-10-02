# 1 - Getting key with maximum value in dictionary:
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

def filter_by_order(orders, order):
    return filter_orders(orders, 'order', order)


def filter_by_client(orders, client):
    return filter_orders(orders, 'client', client)


def filter_orders(all_orders, field, value):
    filtered_orders = list(filter(
        lambda order: order[field] == value, all_orders
    ))
    return filtered_orders


def get_values_from_field(all_orders, field):
    values_list = []
    for order in all_orders:
        if order[field] not in values_list:
            values_list.append(order[field])
    return values_list


def find_most_repeated_value(all_orders, field):
    fieldValueDict = {}
    for order in all_orders:
        value = order[field]
        if value not in fieldValueDict:
            fieldValueDict[value] = 1
        else:
            fieldValueDict[value] += 1
    return max(fieldValueDict, key=fieldValueDict.get)  # 1


def find_less_repeated_value(all_orders, field):
    fieldValueDict = {}
    for order in all_orders:
        value = order[field]
        if value not in fieldValueDict:
            fieldValueDict[value] = 1
        else:
            fieldValueDict[value] += 1
    return min(fieldValueDict, key=fieldValueDict.get)  # 1
