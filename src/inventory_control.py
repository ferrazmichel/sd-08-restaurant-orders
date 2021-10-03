class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }

    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        if not self.__is_dish_available(order):
            return False
        self.orders.append({"client": costumer, "item": order, "day": day})

    def get_quantities_to_buy(self):
        items_to_buy = {
            key: 0 for key in InventoryControl.MINIMUM_INVENTORY.keys()
        }

        items = [order["item"] for order in self.orders]

        for item in items:
            for igredient in InventoryControl.INGREDIENTS[item]:
                items_to_buy[igredient] += 1

        return items_to_buy

    def __is_dish_available(self, dish_name):
        quantities_to_buy = self.get_quantities_to_buy()
        for ingredient in InventoryControl.INGREDIENTS[dish_name]:
            if (
                quantities_to_buy[ingredient]
                >= InventoryControl.MINIMUM_INVENTORY[ingredient]
            ):
                return False
        return True

    def get_available_dishes(self):
        return {
            dish
            for dish in InventoryControl.INGREDIENTS
            if self.__is_dish_available(dish)
        }
