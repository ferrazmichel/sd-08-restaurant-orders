from statistics import mode, median_low


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
        todos_pedidos = set()
        costumer_pediu = set()
        for valor in self.orders:
            todos_pedidos.add(valor[1])
        for valor in self.orders:
            if valor[0] == costumer:
                costumer_pediu.add(valor[1])
        return todos_pedidos-costumer_pediu

    def get_days_never_visited_per_costumer(self, costumer):
        todos_dias = set()
        costumer_visitou = set()
        for valor in self.orders:
            todos_dias.add(valor[2])
        for valor in self.orders:
            if valor[0] == costumer:
                costumer_visitou.add(valor[2])
        return todos_dias-costumer_visitou

    def get_busiest_day(self):
        todos_dias = []
        for valor in self.orders:
            todos_dias.append(valor[2])
        return mode(todos_dias)

    def get_least_busy_day(self):
        todos_dias = []
        for valor in self.orders:
            todos_dias.append(valor[2])
        return median_low(todos_dias)
