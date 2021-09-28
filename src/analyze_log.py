import csv


def analyze_log(path_to_file):
    # raise NotImplementedError
    # Qual o prato mais pedido por 'maria'?
    # maria está na primeira posição

    with open(path_to_file) as csv_file:
        csv_reader = tuple(csv.reader(csv_file, delimiter=','))
        # print(csv_reader[0][0])
        menu = []
        joao_orders = []
        joao_days = []
        
        count_maria_food = []
        arnaldo_hamburguers = 0
        for item in csv_reader:
            menu.append(item[1])
            menu = list(dict.fromkeys(menu))

            if item[0] == 'maria':
                # count_maria_food["maria"] = item[1]
                count_maria_food.append(item[1])
            elif item[0] == 'arnaldo' and item[1] == 'hamburguer':
                arnaldo_hamburguers += 1
            elif item[0] == 'joao':
                joao_orders.append(item[1])
        
        print(f'Prato mais pedido por Maria {max(count_maria_food)}') 
        print(f'Arnaldo Burger {arnaldo_hamburguers}')
        print(f'joao nunca pediu {set(menu) - set(joao_orders)}')
        print(f'joao_orders {joao_orders}')
        print(f'menu {menu}')
        
        
        
        # print(maria_food, arnaldo_hamburguers)

        

analyze_log('./data/orders_1.csv')
