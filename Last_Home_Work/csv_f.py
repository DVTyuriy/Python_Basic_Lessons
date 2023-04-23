import csv


class Csv:
    @staticmethod
    def read_csv(csv_file: str) -> list:
        """
        Фунція відкритя csv файлу
        :param csv_file: найменування файлу
        :return: зміст файлу ввиді списку
        """
        csv_file1 = 'SKU\\' + csv_file
        with open(csv_file1, 'r') as f:
            read = list(csv.DictReader(f))
            return read
