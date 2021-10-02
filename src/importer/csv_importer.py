import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        converted_file = []
        with open(path) as file:
            file_readed = csv.reader(file, delimiter=",", quotechar='"')
            for row in file_readed:
                client, order, day = row
                converted_file.append(
                    {'client': client, 'order': order, 'day': day}
                )
        return converted_file
