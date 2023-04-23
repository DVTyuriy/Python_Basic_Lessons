from .csv_f import Csv
from .json_f import Json
from datetime import datetime
import operator


class FileProcessor:
    def __init__(self, date: str, time: str, sku: str, warehouse: str,
                 warehouse_cell_id: str, operation: str, invoice: str,
                 expiration_date: str, operation_cost: str, comment: str):
        self.date = date
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment

    @staticmethod
    def append_f(list1: list) -> list:
        """
        Функція відкриття файлів, та додаємо зміст файлів до списку
        :param list1: список файлів
        :return: зміст файлів
        """
        list_full = list()
        for j in list1:
            # перевіряємо розширення файлу
            if j.endswith('.csv'):
                # додаємо зміст до файлу
                list_full.append(Csv.read_csv(j))
            # перевіряємо розширення файлу
            elif j.endswith('.json'):
                # додаємо зміст до файлу
                list_full.append(Json.read_json(j))
        return list_full

    @staticmethod
    def index_tab(list1: list, comment1: str) -> dict:
        """
        Фунція індексації даних
        :param list1: список, який потрібно обробити
        :param comment1: параметр для індексації
        :return: словних індексованих данних по параметру
        """
        i_index = dict()
        for row in list1:
            for ind in row:
                if ind[comment1] not in i_index:
                    i_index[ind[comment1]] = list()
                i_index[ind[comment1]].append(ind)
        return i_index

    @staticmethod
    def sale(list1: list) -> float:
        """
        Фунція. яка рахує вартість всіх успіхних операцій
        :param list1: список всїх операцій
        :return: вартість всіх успіхних операцій
        """
        i_index = float()
        for row in list1:
            for ind in row:
                if 'sale' in ind['operation']:
                    i_index += float(ind.get('operation_cost'))
        return i_index

    @staticmethod
    def expire_date(list1: list) -> int:
        """
         Фунція. яка рахує, скільки унікальних SKU було втрачено
        :param list1: список всїх операцій
        :return: скільки унікальних SKU було втрачено
        """
        ind_sku = set()
        for row in list1:
            for ind in row:
                if datetime.now() > datetime.strptime(ind['expiration_date'], "%d-%b-%Y"):
                    if ind['operation'] != 'sale':
                        ind_sku.add(ind['sku'])
        ind_sku = len(ind_sku)
        return ind_sku

    @staticmethod
    def how_to_warehouse(list1: list) -> dict:
        """
        Фунція. яка рахує, скільки товарів "пройшло" через кожний склад
        :param list1: список всїх операцій
        :return: скільки товарів "пройшло" через кожний склад в сортованому вигляді
        """
        population = dict()
        for row in list1:
            for ind in row:
                if ind['warehouse'] not in population:
                    population[ind['warehouse']] = 0
                population[ind['warehouse']] += 1
        population = dict(sorted(population.items(), key=operator.itemgetter(0)))
        return population

    @staticmethod
    def how_to(list1: list, text: str) -> dict:
        """
        Фунція. яка рахує кількість товарів, в залежності від операції
        :param list1: список всїх операцій
        :param text: вид операції
        :return: операцій на складі в залежності від операції в сортованому вигляді
        """
        population = dict()
        for row in list1:
            for ind in row:
                if ind['operation'] == text:
                    if ind['warehouse'] not in population:
                        population[ind['warehouse']] = 0
                    population[ind['warehouse']] += 1
        population = dict(sorted(population.items(), key=operator.itemgetter(0)))
        return population
