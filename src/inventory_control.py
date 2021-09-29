class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho", "tomate"],
        "queijo-quente": ["pao", "queijo", "queijo"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "bauru": ["pao", "queijo", "presunto", "tomate"],
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
        self.ingredients_to_buy = {}
        self.available_dishes = set()
        for key in self.MINIMUM_INVENTORY.keys():
            self.ingredients_to_buy[key] = 0
        for key in self.INGREDIENTS.keys():
            self.available_dishes.add(key)

    def remove_available_dishes_by_ingredient(self, ingredient):
        for key, value in self.INGREDIENTS.items():
            if ingredient in value:
                self.available_dishes.discard(key)

    def remove_available_dishes(self, order):
        for ingredient in self.INGREDIENTS[order]:
            if ingredient in self.MINIMUM_INVENTORY:
                if (
                    self.ingredients_to_buy[ingredient] + 1
                    > self.MINIMUM_INVENTORY[ingredient]

                ):
                    self.available_dishes.discard(order)
                    self.remove_available_dishes_by_ingredient(ingredient)

    def add_new_order(self, costumer, order, day):
        if order not in self.available_dishes:
            return False
        self.remove_available_dishes(order)
        if order in self.available_dishes:
            for ingredient in self.INGREDIENTS[order]:
                if ingredient in self.MINIMUM_INVENTORY:
                    self.ingredients_to_buy[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.ingredients_to_buy

    def get_available_dishes(self):
        return self.available_dishes
