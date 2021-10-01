from csv import DictReader
from statistics import mode


def get_produto_mais_pedido_por_maria(lista_de_pedidos):
    produtos_pedidos_por_maria = [
        pedido['produto']
        for pedido in lista_de_pedidos if pedido['nome'] == 'maria'
    ]

    return mode(produtos_pedidos_por_maria)


def get_qtd_de_burgers_de_arnaldo(lista_de_pedidos, produto):
    produtos_pedidos_arnaldo = [
        pedido['produto']
        for pedido in lista_de_pedidos if pedido['nome'] == 'arnaldo'
    ]

    return produtos_pedidos_arnaldo.count(produto)


def analyze_log(path_to_file):
    if not path_to_file or not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    with open(path_to_file, 'r') as orders_1:
        lista_de_pedidos = list(DictReader(
            orders_1,
            fieldnames=['nome', 'produto', 'dia_semana']
            )
        )

    produto_mais_pedido_por_maria = get_produto_mais_pedido_por_maria(
        lista_de_pedidos
        )

    qtd_de_burgers_de_arnaldo = get_qtd_de_burgers_de_arnaldo(
        lista_de_pedidos,
        'hamburguer'
        )

    todos_os_produtos = set([order['produto'] for order in lista_de_pedidos])
    dias_da_semana = set([order['dia_semana'] for order in lista_de_pedidos])

    produtos_joao_nunca_pediu = set()
    dias_joao_nunca_foi_na_lanchonete = set()

    for order in lista_de_pedidos:
        if order['nome'] == 'joao':
            produtos_joao_nunca_pediu.add(order['produto'])
            dias_joao_nunca_foi_na_lanchonete.add(order['dia_semana'])

    with open('data/mkt_campaign.txt', 'w') as output_file:
        output_file.write(
            f'{produto_mais_pedido_por_maria}\n'
            f'{qtd_de_burgers_de_arnaldo}\n'
            f'{todos_os_produtos.difference(produtos_joao_nunca_pediu)}\n'
            f'{dias_da_semana.difference(dias_joao_nunca_foi_na_lanchonete)}'
        )
