import json


class Json:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def __str__(self):
        return self.csv_file

    def read_json(csv_file: str) -> list:
        csv_file1 = 'SKU\\' + csv_file
        d = json.load(open(csv_file1, 'r'))
        data = d['data']
        return data
