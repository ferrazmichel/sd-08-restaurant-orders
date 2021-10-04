from src.Order_Analyzer import OrderAnalyzer


def analyze_log(path_to_file):
    analyzer = OrderAnalyzer(path_to_file)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(analyzer.most_ordered_by_client_name('maria') + '\n')
        file.write(str(
            analyzer.quantity_of_dish_by_client_name('arnaldo', 'hamburguer'))
            + '\n')
        file.write(str(
            analyzer.never_occurred_data_by_client_name('joao', 'dish_name'))
            + '\n')
        file.write(str(
            analyzer.never_occurred_data_by_client_name('joao', 'week_day'))
            + '\n')
