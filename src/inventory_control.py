class InventoryControl:
    MENU = {"hamburguer", "pizza", "misto-quente", "coxinha"}

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

    CONTROL_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    GET_INGREDIENTS = {
        "pao": 0,
        "carne": 0,
        "queijo": 0,
        "molho": 0,
        "presunto": 0,
        "massa": 0,
        "frango": 0,
    }

    def __init__(self):
        self.order_data = {}

    def add_new_order(self, costumer, order, day):
        one_order = {"Nome": costumer, "Pedido": order, "Dia": day}
        self.order_data = one_order
        if self.check_sotck() is False:
            return False
        self.remove_from_sotck()
        self.use_ingredient()
        return True

    def get_available_dishes(self):
        # print(self.order_data["Pedido"])
        # for ingredient in self.INGREDIENTS[self.order_data["Pedido"]]:
        #     print("print", self.MINIMUM_INVENTORY)
        #     if (
        #         self.CONTROL_INVENTORY[ingredient] > 0
        #         and self.order_data["Pedido"] in self.MENU
        #     ):
        #         return self.MENU
        #     else:
        #         print("Vou remover")
        #         self.MENU.remove(self.order_data["Pedido"])
        return self.MENU

    def check_sotck(self):
        print(self.order_data)
        for ingredient in self.INGREDIENTS[self.order_data["Pedido"]]:
            if self.CONTROL_INVENTORY[ingredient] == 0:
                return False

    def remove_from_sotck(self):
        print(self.order_data)
        for ingredient in self.INGREDIENTS[self.order_data["Pedido"]]:
            # print(ingredient)
            if self.CONTROL_INVENTORY[ingredient] > 0:
                self.CONTROL_INVENTORY[ingredient] -= 1
        print(self.GET_INGREDIENTS)

    def use_ingredient(self):
        for ingredient in self.INGREDIENTS[self.order_data["Pedido"]]:
            self.GET_INGREDIENTS[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.GET_INGREDIENTS
