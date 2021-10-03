def analyze_log(path_to_file):
    with open(path_to_file) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines if 'maria' in line]
        my_dict = {i: lines.count(i) for i in lines}
        max_key = max(my_dict, key=my_dict.get)
        maria = max_key.split(',')[1]
        result = open('data/mkt_campaign.txt', 'a')
        result.write(maria)

# print(analyze_log('/home/tandy/trybe/projects/computer-science/sd-08-restaurant-orders/data/orders_1.csv'))
