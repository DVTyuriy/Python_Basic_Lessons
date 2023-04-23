import json


class Json:
    @staticmethod
    def read_json(json_file: str) -> list:
        """
        Фунція відкритя csv файлу
        :param json_file: найменування файлу
        :return: зміст файлу ввиді списку
        """
        json_file1 = 'SKU\\' + json_file
        d = json.load(open(json_file1, 'r'))
        data = d['data']
        return data
