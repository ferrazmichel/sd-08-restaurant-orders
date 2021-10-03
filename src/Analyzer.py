from csv import DictReader
from collections import Counter


class Analyzer:
    def __init__(self, path):
        with open(path) as file:
            self.log_data = list(
                DictReader(file, fieldnames=["client", "item", "day"])
            )

    def __get_orders_by_name(self, name):
        return filter(lambda order: order["client"] == name, self.log_data)

    def __get_menu_items(self):
        return {order["item"] for order in self.log_data}

    def __get_work_days(self):
        return {order["day"] for order in self.log_data}

    def __maria_favorites(self):
        items = [order["item"] for order in self.__get_orders_by_name("maria")]
        counter = Counter(items)
        return counter.most_common(1).pop()[0]

    def __arnaldo_burger_count(self):
        return sum(
            order["item"] == "hamburguer"
            for order in self.__get_orders_by_name("arnaldo")
        )

    def __joao_must_try_items(self):
        menu = self.__get_menu_items()
        joaos_items = {
            order["item"] for order in self.__get_orders_by_name("joao")
        }
        return menu - joaos_items

    def __joao_healthy_days(self):
        joaos_days = {
            order["day"] for order in self.__get_orders_by_name("joao")
        }
        return self.__get_work_days() - joaos_days

    def analyze(self, output_path):
        with open(output_path, "w") as file:
            for action in (
                self.__maria_favorites,
                self.__arnaldo_burger_count,
                self.__joao_must_try_items,
                self.__joao_healthy_days,
            ):
                print(action(), file=file)
