from statistics import mode

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.orders

    def get_most_ordered_dish_per_costumer(self, costumer):
        pedido = []
        for valor in self.orders:
            if valor[0] == costumer:
                pedido.append(valor[1])
        return mode(pedido)

    def get_never_ordered_per_costumer(self, costumer):
        # nunca_pediu = set()
        # nunca_pediu = set()
        for valor in self.orders:
            print("valor")
            print(valor[1])
        #     nunca_pediu.add(valor[0][1])
        # print(nunca_pediu)
        # return nunca_pediu


    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

# 2.4 - Será validado se, ao executar get_never_ordered_per_costumer, o método retorna o pedido que o cliente nunca fez.

# 2.5 - Será validado se, ao executar get_days_never_visited_per_costumer, o método retorna o dias que o cliente nunca visitou.

# 2.6 - Será validado se, ao executar o método get_busiest_day, o método retorna o dia mais movimentado.

# 2.7 - Será validado se, ao executar o método get_least_busy_day, o método retorna o dia menos movimentado.
