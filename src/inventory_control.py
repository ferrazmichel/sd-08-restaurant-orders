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
        self.inventory = self.MINIMUM_INVENTORY.copy()
        self.order_list = []
        self.available_dishes = set(self.INGREDIENTS.keys())
        self.available_ingredients = set(self.inventory.keys())

    def add_new_order(self, costumer, order, day):
        if order not in self.get_available_dishes():
            return False

        self.order_list.append(
            {"costumer": costumer, "order": order, "day": day}
        )

        for ingredient in self.INGREDIENTS[order]:
            self.inventory[ingredient] -= 1

            if self.inventory[ingredient] < 1:
                self.available_ingredients.remove(ingredient)

    def get_quantities_to_buy(self):
        minimum = self.MINIMUM_INVENTORY
        current = self.inventory

        return {k: minimum[k] - current[k] for k in list(minimum.keys())}

    def get_available_dishes(self):
        for dish in self.available_dishes.copy():
            if not set(self.INGREDIENTS[dish]) <= self.available_ingredients:
                self.available_dishes.remove(dish)

        return self.available_dishes
