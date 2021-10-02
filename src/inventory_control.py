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
        self.ingredients_stock = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

    def add_new_order(self, costumer, order, day):
        available_dishes = self.get_available_dishes()
        if order not in available_dishes:
            return False
        used_ingredients = self.INGREDIENTS[order]
        for ingredient in used_ingredients:
            self.ingredients_stock[ingredient] -= 1
        self.orders.append([costumer, order, day])

    def get_quantities_to_buy(self):
        return {
            ing: self.MINIMUM_INVENTORY[ing] - self.ingredients_stock[ing]
            for ing in self.ingredients_stock
        }

    def get_available_dishes(self):
        available_ingredients = {
            ing
            for ing in self.ingredients_stock
            if self.ingredients_stock[ing] > 0
        }
        return {
            recipe
            for recipe in self.INGREDIENTS
            if available_ingredients.issuperset(self.INGREDIENTS[recipe])
        }
