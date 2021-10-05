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

    def add_new_order(self, costumer, order, day):
        self.order_list.append(
            {"costumer": costumer, "order": order, "day": day}
        )

        for ingredient in self.INGREDIENTS[order]:
            self.inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        minimum = self.MINIMUM_INVENTORY
        current = self.inventory

        return {k: minimum[k] - current[k] for k in list(minimum.keys())}
