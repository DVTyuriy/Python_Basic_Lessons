import csv


def open_f() -> list:
    """
    Функція відкриття csv файлу
    :return: повертає список словарів
    """
    with open('tech_inventory.csv', 'r', newline='') as csvfile:
        r = csv.DictReader(csvfile)
        new_dict = list(r)
        return new_dict


def counter(dic: list, br: str, br_1: str) -> dict:
    """
    Функція, яка підраховує кількість товарів за вказаним фільтром br
    та викликає функцію друку на екран
    :param dic: сприймає список словарів
    :param br: назва стовбця, по якій буде підрахунок
    :param br_1: текст для принту на екрані
    :return: словник
    """
    population = dict()
    for category in dic:
        if category[br] not in population:
            population[category[br]] = 0
        population[category[br]] += 1
    printer(population, br_1)
    return population


def counter_br(dic: list, br6: str):
    """
    Функція, яка підраховує кількість товарів за вказаним фільтром brand
    :param dic: сприймає список словників
    :param br6: Слово для виводу на екран
    """
    population_br = dict()
    for category in dic:
        if category['brand'] not in population_br:
            population_br[category['brand']] = 0
        population_br[category['brand']] += 1
    print(f'У категорії {br6} представлені товари таких брендів:')
    print(population_br, '\n')


def printer(dic_print: dict, tex: str):
    """
    Функція друку на екран
    :param dic_print: словник, який необхідно роздрукувати
    :param tex:передаємо текст для друку на екрані
    """
    for value in dic_print:
        print(tex, value, 'є', dic_print.get(value, 0), 'товарів')
    print()


def printer_list(print_br: str, dic_print: list, print_br1: str):
    """
    Функція друку на екран
    :param print_br: назва категорії, друкується для інформативності
    :param dic_print: Список, який потрібно роздрукувати
    :param print_br1: передаємо текст для друку на екрані
    """
    print(print_br1, print_br)
    for value1 in dic_print:
        print(value1)
    print()


def brand(dic1: list, br1: str):
    """
    Функція, яка зі списку словників вибирає інформацію про певний бренд
    та передає на в іншу функцію
    :param dic1: сприймає список словників
    :param br1: певний бренд
    """
    res_br1 = list(filter(lambda item: item['brand'] == br1, dic1))
    printer_list(br1, res_br1, 'Бренд')


def cat(dic2: list, br2: str):
    """
    Функція, яка зі списку словників виберає інформацію про певну категорію
    та передає на в іншу функцію
    :param dic2: сприймає список словників
    :param br2: певна категорія
    """
    res_br2 = list(filter(lambda item: item['category'] == br2, dic2))
    printer_list(br2, res_br2, 'Категорія')


def cat_list(dic2: list, br2: str) -> list:
    """
    Функція, яка зі списку словників виберає інформацію про певну категорію
    та передає на в іншу функцію
    :param dic2: сприймає список словників
    :param br2: певна категорія
    :return: повертає список
    """
    res_br2 = list(filter(lambda item: item['category'] == br2, dic2))
    return res_br2


def input_cat(pbrand: dict, pcat: dict):
    """
    Функція сорту по бренду або категорії
    :param pbrand: словник брендів
    :param pcat: словник категорій
    """
    while True:
        name = str(input('Введіть введіть бренд або категорію для перегляду спуску товарів, для продовження "END"\n'))
        if name.lower() in 'end':
            break
        if name in pbrand:
            # викликаємо функцію перелік повної інформації про кожний товар одного обраного бренда
            brand(dict_csv, name)
        elif name.title() in pcat:
            # викликаємо функцію перелік повної інформації про кожний товар однієї обраної категорії.
            cat(dict_csv, name)
        else:
            print('Зуськи, нема такого, давай спробуємо ще раз, або введи "END"\n')


if __name__ == '__main__':
    # викликаємо функцію зчитування з файла csv
    dict_csv = open_f()
    # викликаємо функцію підрахунок товару по бренду
    pop_brand = counter(dict_csv, 'brand', 'Від бренду')
    # викликаємо функцію підрахунок товару по категорії
    pop_cat = counter(dict_csv, 'category', 'Серед категорії')
    # викликаємо функцію для перегляду або по категорії або по бренду
    input_cat(pop_brand, pop_cat)
    # створення списків по категоріям
    list_laptop = cat_list(dict_csv, 'Laptop')
    list_comp = cat_list(dict_csv, 'Computer Mouse')
    list_smart = cat_list(dict_csv, 'Smartphones')
    list_keyb = cat_list(dict_csv, 'Keyboard')
    # викликає функцію підрахунок кількість брендів в певній категорії
    counter_br(list_laptop, 'Laptop')
    counter_br(list_comp, 'Computer Mouse')
    counter_br(list_smart, 'Smartphones')
    counter_br(list_keyb, 'Keyboard')
