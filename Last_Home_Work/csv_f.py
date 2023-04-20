import csv

class Csv:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def __str__(self):
        return self.csv_file

    def read_csv(csv_file: str) -> list:
        csv_file1 = 'SKU\\' + csv_file
        with open(csv_file1, 'r') as f:
            read = list(csv.DictReader(f))
            return read



