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
        """Retorna um dict com o prato mais pedido pelo cliente"""
        # costumer=costumer, order=order, day=day

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
