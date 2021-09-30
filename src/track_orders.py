from collections import Counter


class TrackOrders:
    # self representa a instância da classe.
    # Usando a palavra-chave “self”, podemos acessar
    # os atributos e métodos da classe em python
    # Ele vincula os atributos aos argumentos fornecidos
    # Após entender isto ficou mais fácil fazer os métodos
    # "conversarem".
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        """Adiciona o cliente, o pedido e o dia à
        lista orders"""
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        """Retorna o prato mais pedido pelo cliente"""
        more_ordered = []

        for item in self.orders:
            if item[0] == costumer:
                more_ordered.append(item[1])
            costumer_dict = Counter(more_ordered)
        # retorna a chave com o maior valor
        # https://www.ti-enxame.com/pt/python/encontrar-o-maior-valor-em-um-dicionario/1069289117/
        return max(costumer_dict, key=costumer_dict.get)

    def get_never_ordered_per_costumer(self, costumer):
        """Este método utilizou a mesma lógica do 
        analyze_log no quesito 'joao_never_asked' """
        costumer_orders = set()
        menu = set()
        for item in self.orders:
            menu.add(item[1])
            if item[0] == costumer:
                costumer_orders.add(item[1])
        return set(menu) - set(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
