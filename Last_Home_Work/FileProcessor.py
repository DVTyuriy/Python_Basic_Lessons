from .csv_f import Csv
from .json_f import Json


class FileProcessor:
    def __init__(self, date: str, time: str, sku: str, warehouse: str,
                 warehouse_cell_id: str, operation: str, invoice: str,
                 expiration_date: str, operation_cost: str, comment: str, file: str):
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
        self.file = 'list_files.txt'

    def __str__(self):
        return self.date, self.time, self.sku, self.warehouse, self.warehouse_cell_id, self.operation, self.invoice, self.expiration_date, self.operation_cost, self.comment

    # os.listdir()
    def open_list_files(file: str) -> list:
        lines = list()
        with open(file, 'r') as f:
           for line in f.readlines():
               lines.append(line.strip())
        return lines

    def append_f(list1: list) -> list:
        list_full = list()
        for j in list1:
            if j.endswith('.csv'):
                list_full.append(Csv.read_csv(j))
            else:
                list_full.append(Json.read_json(j))
        return list_full

    def index_tab(list1: list, comment: str):
        i_index = dict()
        for row in list1:
            for ind in row:
                if ind[comment] not in i_index:
                    i_index[ind[comment]] = list()
                i_index[ind[comment]].append(ind)
        return i_index

    def sale(list1: list):
        i_index = float()
        for row in list1:
            for ind in row:
                if 'sale' in ind['operation']:
                    # print(ind)
                    # print(ind.get('operation_cost'))
                    i_index += float(ind.get('operation_cost'))
        return i_index











