from src.Analyzer import Analyzer
from csv import DictReader


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        data = list(DictReader(file, fieldnames=["client", "item", "day"]))
    analyzer = Analyzer(data)
    analyzer.analyze("data/mkt_campaign.txt")
