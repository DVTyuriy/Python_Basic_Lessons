COMMAND = [
    'Введіть:',
    'open -     відкрити та прочитати всі записи',
    'add -      для додавання нотаток',
    'earliest - щоб вивести нотатки на экран від найранішої до найпізнішої:',
    'latest -   щоб вивести нотатки на экран від найпізнішої до найранішої:',
    'longest -  щоб вивести нотатки на экран від найдовшої до найкоротшої:',
    'shortest - щоб вивести нотатки на экран від найкоротшої до найдовшої:',
    'exit -     для збереження та завершення програми'
]


def open_f() -> list:
    """
    Функія відкриття файлу з нотатками
    :return: вертає прочитану інфу з файла
    """
    lines = list()
    # відкриваємо файл та зчитуємо інформацію
    while True:
        try:
            with open(name_save_open(), 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    lines.append(line.strip())
                print('Файл було прочитано')
                return lines
        except Exception:
            print('Дідко, не можу прочитати цей файл, давай прочитаємо інший, або створимо нові нотатки')
            print()
            # вертаємо пустий список, якщо не змогли прочитати файл
            return lines


def save_f(tuple_to_save: tuple):
    """
    Функція, яка зберігає інформацію до файлу при виході з програми
    :param tuple_to_save: Кортеж з нотатками
    :return: нічого не повертаємо, виходимо з програми
    """
    list_to_save = list(tuple_to_save)
    # зберігаємо введену/зчитану інформацію до файлу
    with open(name_save_open(), 'w', encoding='utf-8') as write_f:
        text = '\n'.join(list_to_save)
        write_f.write(text)
    print('Інформацію було збережено')


def name_save_open() -> str:
    """
    Функція для вводу назви файлу при відкритті/збереженні
    :return: повертаємо назву файла
    """
    return input('Ведіть назву файла: ')


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
    print(comment)
    for note in input_list_print[:n]:
        print(note)
    print('=' * 10, 'New operation', '=' * 10)


def input_num() -> int:
    """
    Функція для зчитування кількості необхідних рядків для виведеня на екран
    :return: кількість рядків
    """
    while True:
        try:
            k = int(input('Скільки нотатків ви хочете побачити: '))
            if k <= 0:
                print("Не можу сгенерувати від'ємну або нульову нотатків")
                continue
            return k
        except Exception:
            print('Трясся, я не можу сприйняти це як число')


def print_ln():
    """
    Функція для виведення на екран команд для взаємодії
    :return: функція нічого не повертає, а лише виводить на екран інформацію зі списку
    """
    for j in COMMAND:
        print(j)


if __name__ == '__main__':
    # об`являємо змінні
    contain_tuple = tuple()
    contain_list = list()
    while True:
        # виводимо інфу  для взаємодії с користувачем
        print_ln()
        # інпут нотатків від юзера, або команди на обробку нотатків
        input_word = input()

        # Якщо було введено 'open', відкриваємо файл та читаємо його, записуємо в кортеж
        if input_word == 'open':
            contain_list += open_f()
            contain_tuple = tuple(contain_list)

        # Якщо було введено 'add', то додаємо наступний введений текст до нотатків
        elif input_word == 'add':
            print('Введіть текст для додавання в нотатки')
            input_list = input()
            # якщо нічого не було введено, нічого не додаємо до нотатків
            if not input_list:
                pass
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
            print()

        # перевірка, якщо юзер хоче відсортувати від найпізнішої до найранішої
        elif input_word.lower() == 'latest':
            latest(contain_tuple, 'Від найпізнішої до найранішої:')
            print()

        # перевірка, якщо юзер хоче відсортувати від найдовшої до найкоротшої
        elif input_word.lower() == 'longest':
            longest_short(contain_tuple, True, 'Від найдовшої до найкоротшої:')
            print()

        # перевірка, якщо юзер хоче відсортувати від найкоротшої до найдовшої
        elif input_word.lower() == 'shortest':
            # показуємо, що ми хочемо сортувати в залежності від довжини елемента списку
            longest_short(contain_tuple, False, 'Від найкоротшої до найдовшої:')
            print()

        # перевірка, якщо юзер хоче вийти та зберегти данні
        elif input_word.lower() == 'exit':
            save_f(contain_tuple)
            exit()

        # перевірка, якщо юзер ввів не команду
        else:
            print('Нічого не зрозуміло, але дуже цікаво. Введіть команду для для виконання необхідних дії')
            print()
