class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }
    CURRENT_INVENTORY = {}

    def __init__(self):
        for item in self.MINIMUM_INVENTORY:
            self.CURRENT_INVENTORY[item] = self.MINIMUM_INVENTORY[item]
        pass

    def add_new_order(self, _costumer, order, _day):
        ingredients_used = self.INGREDIENTS[order]

        for item in ingredients_used:
            if self.CURRENT_INVENTORY[item] == 0:
                return False
            if item in ingredients_used:
                self.CURRENT_INVENTORY[item] -= 1
        pass

    def get_quantities_to_buy(self):
        itens_to_buy = {}
        for item in self.CURRENT_INVENTORY:
            quantity_used = self.CURRENT_INVENTORY[item]
            itens_to_buy[item] = self.MINIMUM_INVENTORY[item] - quantity_used
        return itens_to_buy

    def get_available_dishes(self):
        restaurant_menu = list(self.INGREDIENTS.keys())
        available_dishes = set()
        for meal in restaurant_menu:
            ingredients_used = self.INGREDIENTS[meal]
            all_available = True
            for item in ingredients_used:
                if self.CURRENT_INVENTORY[item] == 0:
                    all_available = False
            if all_available:
                available_dishes.add(meal)
        return available_dishes
