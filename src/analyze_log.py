import csv
from statistics import mode
def analyze_log(path_to_file):
    nome = {}
    pedido = set()
    dia = set()

    with open(path_to_file, "r") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')
        for valor in data:
            pedido.add(valor[1])
            dia.add(valor[2])
            if valor[0] not in nome:
                nome[valor[0]] = [(valor[1], valor[2])]
            else:
                nome[valor[0]].append((valor[1], valor[2]))
    
    maria = []
    for valor in nome["maria"]:
        maria.append(valor[0])
    maria_maior = mode(maria)

    arnaldo = 0
    for valor in nome["arnaldo"]:
        if valor[0] == "hamburguer":
            arnaldo += 1
    print(maria_maior)
    print(arnaldo)
    print(nome)


# Quantas vezes 'arnaldo' pediu 'hamburguer'?

# Quais pratos 'joao' nunca pediu?

# Quais dias 'joao' nunca foi na lanchonete?

# hamburguer
# 1
# {'pizza', 'coxinha', 'misto-quente'}
# {'sabado', 'segunda-feira'}
