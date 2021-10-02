from statistics import mode
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.encomendas = []

    def __len__(self):
        return len(self.encomendas)

    def add_new_order(self, costumer, order, day):
        self.encomendas.append(
            {'costumer': costumer, 'order': order, 'day': day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        return mode(
            encomenda['order']
            for encomenda in self.encomendas
            if encomenda['costumer'] == costumer
        )

    def get_never_ordered_per_costumer(self, costumer):
        todos_os_produtos = set(
            [encomenda['order'] for encomenda in self.encomendas]
        )
        produtos_cliente = set([
            encomenda['order']
            for encomenda in self.encomendas
            if encomenda['costumer'] == costumer
        ])

        return todos_os_produtos.difference(produtos_cliente)

    def get_days_never_visited_per_costumer(self, costumer):
        dias_da_semana = set(
            [encomenda['day'] for encomenda in self.encomendas]
        )
        dias_cliente_nunca_visitou = set([
            encomenda['day']
            for encomenda in self.encomendas
            if encomenda['costumer'] == costumer
        ])

        return dias_da_semana.difference(dias_cliente_nunca_visitou)

    def get_busiest_day(self):
        return mode(
            encomenda['day'] for encomenda in self.encomendas
        )

    def get_least_busy_day(self):
        ocorrencias = Counter(
            encomenda['day'] for encomenda in self.encomendas
        ).most_common()

        menores_ocorrencias = ocorrencias[-1]

        return menores_ocorrencias[0]
