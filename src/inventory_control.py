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
        self.data = []
        self.ingredients = self.MINIMUM_INVENTORY.copy()
        pass

    def add_new_order(self, costumer, order, day):
        self.data.append([costumer, order, day])
        list_ingredients = self.INGREDIENTS[order]
        for item in list_ingredients:
            if self.ingredients[item] > 0:
                self.ingredients[item] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        result = {}
        for item in self.MINIMUM_INVENTORY:
            print(self.MINIMUM_INVENTORY[item], self.ingredients[item])
            result[item] = (
                self.MINIMUM_INVENTORY[item] - self.ingredients[item]
            )
        return result

    def get_available_dishes(self):
        result = set()
        set_of_ingradients = set(self.ingredients)
        recipes = self.INGREDIENTS
        for recipe in recipes:
            set_rec = set(recipes[recipe])
            # print(set_rec, set_of_ingradients)
            # print(set_rec.issubset(set_of_ingradients))
            if set_rec.issubset(set_of_ingradients):
                result.add(recipe)
        return result
