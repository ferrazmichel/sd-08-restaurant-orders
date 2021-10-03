from src.Analyzer import Analyzer


def analyze_log(path_to_file):
    analyzer = Analyzer(path_to_file)
    analyzer.analyze("data/mkt_campaign.txt")
