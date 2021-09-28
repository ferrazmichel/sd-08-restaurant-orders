import csv
from src.importer import Importer

# method endswith para verificar final da string:
# https://www.w3schools.com/python/ref_string_endswith.asp


class Csv_importer(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise FileNotFoundError(f"No such file or directory: '{path}'")

        with open(path, newline="") as file:
            reader = csv.reader(file)
            data = list(data for data in reader)
            return data
