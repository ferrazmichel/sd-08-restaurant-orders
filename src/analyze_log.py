import csv


def analyze_log(path_to_file):
    #raise NotImplementedError
    #Qual o prato mais pedido por 'maria'?
    #maria está na primeira posição

    with open(path_to_file) as csv_file:
        csv_reader = tuple(csv.reader(csv_file, delimiter=','))
        print(csv_reader)
        for row in csv_reader:
            prato_maria = {}
            if row[0] == 'maria':
                prato_maria['maria'] = row[1]
        print(prato_maria)


analyze_log('./data/orders_1.csv')
