import csv


def analyze_log(path_to_file):
    if not path_to_file or not path_to_file.endswith(".csv"):
        raise ValueError("Path to file is invalid")

    info_list = []

    try:
        with open(path_to_file, "r") as csv_file:
            # ñ precisa ler com DictReader, reader retorna cada linha um array
            # csv_reader = csv.DictReader(csv_file, delimiter=",")
            csv_reader = csv.reader(csv_file, delimiter=",")
            for info in csv_reader:
                info_list.append(info)
        return info_list
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


print(analyze_log("./data/orders_1.csv"))
