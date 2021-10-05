import csv


def most_ordered_dish(logs, person):

    most_ordered = {}

    for log in logs:
        if log[0] == person and log[1] not in most_ordered:
            most_ordered[log[1]] = 1

        elif log[0] == person:
            most_ordered[log[1]] += 1

    # https://stackoverflow.com/a/280156
    return max(most_ordered, key=most_ordered.get)


def count_repeated_dish(logs, person, dish):

    times_ordered = 0

    for log in logs:
        if log[0] == person and log[1] == dish:
            times_ordered += 1

    return times_ordered


def never_ordered_by_person(logs, person):

    all_dishes = set()
    person_dishes = set()

    for log in logs:
        all_dishes.add(log[1])

        if log[0] == person:
            person_dishes.add(log[1])

    return all_dishes.difference(person_dishes)


def days_out(logs, person):

    restaurant_days = set()
    person_days = set()

    for log in logs:
        restaurant_days.add(log[2])

        if log[0] == person:
            person_days.add(log[2])

    return restaurant_days.difference(person_days)


def write_mkt_campaign(path, datas):

    with open(path, 'w') as text_file:
        for data in datas:
            text_file.write("{0}\n".format(data))


def read_csv_data(path_to_file):

    with open(path_to_file) as file:
        csv_reader = csv.reader(file)

        csv_content = list(csv_reader)

        return csv_content


def analyze_log(path_to_file):
    data_to_write = []
    campaign_file = 'data/mkt_campaign.txt'

    orders = read_csv_data(path_to_file)

    data_to_write.append(most_ordered_dish(orders, 'maria'))
    data_to_write.append(count_repeated_dish(orders, 'arnaldo', 'hamburguer'))
    data_to_write.append(never_ordered_by_person(orders, 'joao'))
    data_to_write.append(days_out(orders, 'joao'))

    write_mkt_campaign(campaign_file, data_to_write)