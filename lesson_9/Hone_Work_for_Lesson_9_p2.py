def gen_word(list_word: list):
    """
    Функція передає кожне наступне слово з вводу користувача
    :param list_word: речення для перетворення
    :return: кожне наступне слово при запросі
    """
    for i in range(len(list_word)):
        yield list_word[i]


if __name__ == '__main__':
    # інпут від користувача строки
    s = input("Введіть строку для перетворення:\n").split()
    # цикл генерації з строки
    for word in gen_word(s):
        print(word)
