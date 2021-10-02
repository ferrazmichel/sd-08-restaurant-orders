from statistics import mode
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.pedidos.append({
            'costumer': costumer,
            'order': order,
            'day': day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        return mode(
            pedido['order']
            for pedido in self.pedidos
            if pedido['costumer'] == costumer
        )

    def get_never_ordered_per_costumer(self, costumer):
        todos_produtos = set([pedido['order'] for pedido in self.pedidos])
        produtos_cliente = set([
            pedido['order']
            for pedido in self.pedidos
            if pedido['costumer'] == costumer
        ])

        return todos_produtos.difference(produtos_cliente)

    def get_days_never_visited_per_costumer(self, costumer):
        dias_da_semana = set([pedido['day'] for pedido in self.pedidos])
        dias_cliente_nunca_foi_na_lanchonete = set([
            pedido['day']
            for pedido in self.pedidos
            if pedido['costumer'] == costumer
        ])

        return dias_da_semana.difference(dias_cliente_nunca_foi_na_lanchonete)

    def get_busiest_day(self):
        return mode(
            pedido['day'] for pedido in self.pedidos
        )

    def get_least_busy_day(self):
        # https://pt.stackoverflow.com/questions/456224/obter-o-elemento-mais-frequente-e-menos-frequente-de-uma-lista-al%C3%A9m-do-maior-e
        frequencias = Counter(
            pedido['day'] for pedido in self.pedidos
        ).most_common()

        menos_frequente = frequencias[-1]

        return menos_frequente[0]
