import abc


class Importer(abc.ABC):
    @abc.abstractclassmethod
    def import_data(path):
        pass
