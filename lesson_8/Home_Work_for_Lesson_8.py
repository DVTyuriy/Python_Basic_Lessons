COMMAND = [
    'Введіть:',
    'add -      для збереження в нотатки',
    'earliest - щоб вивести нотатки на экран від найранішої до найпізнішої:',
    'latest -   щоб вивести нотатки на экран від найпізнішої до найранішої:',
    'longest -  щоб вивести нотатки на экран від найдовшої до найкоротшої:',
    'shortest - щоб вивести нотатки на экран від найкоротшої до найдовшої:',
    'exit -     для завершення'
]


def earliest(earliest_tuple: tuple, comment: str):
    """
    Функція, яка перетворює кортеж на список та передає список на виведення на екран
    :param earliest_tuple: вхідні дані кортеж
    :param comment: коментарій, який потрібний при виведені на екран
    :return: функція нічого не повертає, а лише викликає другу функцію
    """
    earliest_list = list(earliest_tuple)
    printed_for(earliest_list, comment)


def latest(latest_tuple: tuple, comment: str):
    """
    Функція, яка перетворює кортеж на список і робить його в обратному порядку та передає список на виведення на екран
    :param latest_tuple: вхідні дані кортеж
    :param comment: коментарій, який потрібний при виведені на екран
    :return: функція нічого не повертає, а лише викликає другу функцію
    """
    latest_list = list(latest_tuple)
    latest_list.reverse()
    printed_for(latest_list, comment)


def longest_short(longest_tuple: tuple, rev: bool, comment):
    """
    Функція, яка перетворює кортеж на список і сортує за дліною єлемента та передає список на виведення на екран
    :param longest_tuple: вхідні дані кортеж
    :param comment: коментарій, який потрібний при виведені на екран
    :param rev: булька, яка вказує в якому напрямку буде зроблене сортування
    :return: функція нічого не повертає, а лише викликає другу функцію
    """
    longest_list = list(longest_tuple)
    longest_list.sort(key=len, reverse=rev)
    printed_for(longest_list, comment)


def printed_for(input_list_print: list, comment: str):
    """
    Функія, яка виводить на екран список построково
    :param input_list_print: вхідний список
    :param comment: Пояснення до інформації, яку ми виводимо
    :return: функція нічого не повертає, а лише виводить на екран інформацію зі списку
    """
    n = input_num()
    if n > len(input_list_print):
        n = len(input_list_print)
    print(comment)
    for i in range(n):
        print(input_list_print[i])
    print('=' * 10, 'New operation', '=' * 10)


def input_num() -> int:
    """
    Функція для зчитування кількості необхідних рядків для виведеня на екран
    :return: кількість рядків
    """
    while True:
        try:
            k = int(input('Скільки нотатків ви хочете побачити: '))
            return k
        except Exception:
            print('Трясся, я не можу сприйняти це як число')


def print_ln():
    """
    Функція для виведення на екран команд для взаємодії
    :return: функція нічого не повертає, а лише виводить на екран інформацію зі списку
    """
    for j in range(len(COMMAND)):
        print(COMMAND[j])


if __name__ == '__main__':
    # об`являємо змінні
    contain_tuple = tuple()
    contain_list = list()
    while True:
        # виводимо інфу для взаємодії с користувачем
        print_ln()
        # інпут нотатків від юзера, або команди на обробку нотатків
        input_word = input()

        # Якщо було введено 'add', то додаємо наступний введений текст до нотатків
        if input_word == 'add':
            print('Введіть текст для додавання в нотатки')
            input_list = input()
            # якщо нічого не було введено, нічого не додаємо до нотатків
            if input_list == '':
                print('Ви нічого не ввели, а ми нічого не записали:)')
                print()
            else:
                # Додаємо інформацію в список, а список перетворюємо на кортеж
                contain_list.append(input_list)
                contain_tuple = tuple(contain_list)
                print('Так, це ми записали до нотатків')
                print()

        # перевірка, якщо юзер хоче відсортувати від найранішої до найпізнішої
        elif input_word.lower() == 'earliest':
            earliest(contain_tuple, 'Від найранішої до найпізнішої:')

        # перевірка, якщо юзер хоче відсортувати від найпізнішої до найранішої
        elif input_word.lower() == 'latest':
            latest(contain_tuple, 'Від найпізнішої до найранішої:')

        # перевірка, якщо юзер хоче відсортувати від найдовшої до найкоротшої
        elif input_word.lower() == 'longest':
            longest_short(contain_tuple, True, 'Від найдовшої до найкоротшої:')

        # перевірка, якщо юзер хоче відсортувати від найкоротшої до найдовшої
        elif input_word.lower() == 'shortest':
            # показуємо, що ми хочемо сортувати в залежності від довжини елемента списку
            longest_short(contain_tuple, False, 'Від найкоротшої до найдовшої:')

        # перевірка, якщо юзер хоче вийти
        elif input_word.lower() == 'exit':
            exit()

        # перевірка, якщо юзер ввів не команду
        else:
            print('Нічого не зрозуміло, але дуже цікаво. Введіть команду для для виконання необхідних дії')
            print()
