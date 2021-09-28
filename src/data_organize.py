def organize(data):
    """Função organiza o data em analyze_log"""
    initial_days = {
        "segunda-feira": 0,
        "terça-feira": 0,
        "sabado": 0,
    }
    data_client = {}
    for element in data:
        name = element[0]
        food = element[1]
        day = element[3]

        # Usando copy() para copiar de forma rasa um objeto inicial
        # https://docs.python.org/pt-br/3/library/copy.html
        if name not in data_client:
            data_client[name] = {"days": initial_days.copy(), "foods": {}}
        data_client[name]["days"][day] += 1

        if food in data_client[name]["foods"]:
            data_client[name]["foods"][food] += 1
        else:
            data_client[name]["foods"].update({food: 1})
    return data_client


def create_menu(data):
    """Retorna um conjunto Menu"""
    menu = set()
    for item in data.values():
        for food in item["foods"].keys():
            menu.add(food)
    return menu


def popular_food(foods):
    """Retorna a comida mais pedida"""
    return max(foods, key=foods.get)
