from Last_Home_Work import FileProcessor
import os


def open_list_files() -> list:
    """
    Зчитуємо імена файлів з теки та передаємо в змінну
    :return: повертаємо список файлів
    """
    files = os.listdir('SKU')
    return files


if __name__ == '__main__':
    # зчитування списку файлів
    f_list = open_list_files()
    # відкриття файлів та додавання всих файлів до одного файлу
    f_list1 = FileProcessor.append_f(f_list)
    # індексація даних по параметру
    index_sku = FileProcessor.index_tab(f_list1, 'sku')
    index_warehouse = FileProcessor.index_tab(f_list1, 'warehouse')
    index_operation = FileProcessor.index_tab(f_list1, 'operation')
    # робота з даними
    print(f'прибуток від усіх операцій типу sale скдладає: {FileProcessor.sale(f_list1):.2f} UAH')
    print(f'унікальних SKU було втрачено: {FileProcessor.expire_date(f_list1)}')
    print(f'кількість товарів "пройшло" через кожний склад: {FileProcessor.how_to_warehouse(f_list1)}')
    print(f'кількість товарів було продано з кожного складу: {FileProcessor.how_to(f_list1, "sale")}')
    print(f'кількість товарів було утилізовано з кожного складу: {FileProcessor.how_to(f_list1, "dispose")}')
