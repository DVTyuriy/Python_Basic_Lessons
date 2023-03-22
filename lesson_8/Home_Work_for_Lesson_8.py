def printed_for(input_list: list, comment: str):

    print(comment)
    for i in range(len(input_list)):
        print(input_list[i])
    print('=' * 10, 'New operation', '=' * 10)
    input_list = list()


def latest(latest_list: list, comment: str):

    latest_list.reverse()
    printed_for(latest_list, comment)


def longest_short(longest_list: list, rev: bool, comment):
    longest_list.sort(key=len, reverse=rev)
    printed_for(longest_list, comment)


if __name__ == '__main__':
    # об`являємо змінну як список
    contain_list = list()
    ls = list()
    while True:
        # інпут нотатків від юзера, або команди на обробку нотатків
        input_string = input('Введіть текст для збереження в нотатки\n'
                             'Або ви ще маєте вибір\n'
                             'earliest - щоб вивести нотатки на экран від найранішої до найпізнішої:\n'
                             'latest -   щоб вивести нотатки на экран від найпізнішої до найранішої:\n'
                             'longest -  щоб вивести нотатки на экран від найдовшої до найкоротшої:\n'
                             'shortest - щоб вивести нотатки на экран від найкоротшої до найдовшої:\n'
                             'exit -     для завершення\n'
                             )
        # вже набитий список для перевірки
        # contain_list = ['this is note', 'this is notissimo', 'note', 'this is a huge long, insanely long note',
        #                 'well, anyways']

        # перевірка, якщо юзер хоче вийти
        if input_string.lower() == 'exit':
            exit()

        # перевірка, якщо юзер хоче відсортувати від найранішої до найпізнішої
        if input_string.lower() == 'earliest':
            printed_for(contain_list, 'Від найранішої до найпізнішої:')

        # перевірка, якщо юзер хоче відсортувати від найпізнішої до найранішої
        elif input_string.lower() == 'latest':
            latest(contain_list, 'Від найпізнішої до найранішої:')

        # перевірка, якщо юзер хоче відсортувати від найдовшої до найкоротшої
        elif input_string.lower() == 'longest':
            ls = contain_list
            # показуємо, що ми хочемо сортувати в залежності від довжини елемента списку та в зворотньому напрямку
            longest_short(ls, True, 'Від найдовшої до найкоротшої:')

        # перевірка, якщо юзер хоче відсортувати від найкоротшої до найдовшої
        elif input_string.lower() == 'shortest':
            ls = contain_list
            # показуємо, що ми хочемо сортувати в залежності від довжини елемента списку
            longest_short(ls, False, 'Від найкоротшої до найдовшої:')

        # перевірка, якщо юзер не ввів нічого
        elif input_string == '':
            print('Ви нічого не ввели, а ми нічого і не записали')
            print()

        # Якщо нічого не підійшло, то додаємо введений текст до нотатків
        else:
            contain_list.append(input_string)
            print('Так, це ми записали до нотатків')
            ls = contain_list
