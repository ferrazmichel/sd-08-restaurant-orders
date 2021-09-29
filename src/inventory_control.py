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
        self.ingredients = self.INGREDIENTS.copy()
        self.orders = {}

    def add_new_order(self, costumer, order, day):
        order_ingredientes = self.ingredients.get(order)

        temp_inventory = self.inventory.copy()

        for ingrediente in order_ingredientes:
            inventory_ingredient = temp_inventory.get(ingrediente)
            if inventory_ingredient is not None:
                if inventory_ingredient > 0:
                    temp_inventory[ingrediente] -= 1
                else:
                    return False

        self.inventory = temp_inventory.copy()

        if self.orders.get(costumer):
            self.orders[costumer].append({"prato": order, "dia": day})
        else:
            self.orders[costumer] = [{"prato": order, "dia": day}]
        return self.inventory

    def get_quantities_to_buy(self):
        quantities_to_buy = dict()
        for key, value in self.MINIMUM_INVENTORY.items():
            quantities_to_buy[key] = abs(self.inventory[key] - value)

        return quantities_to_buy

    def get_available_dishes(self):
        for recipe_key, recipe_value in self.INGREDIENTS.items():
            for item in recipe_value:
                temp_item = self.inventory.get(item)
                if temp_item == 0 and self.ingredients.get(recipe_key):
                    del self.ingredients[recipe_key]

        return set(self.ingredients.keys())
