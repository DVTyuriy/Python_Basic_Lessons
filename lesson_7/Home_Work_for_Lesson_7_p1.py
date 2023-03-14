# константа зі знаків пунктуації
CONTAINER_UNIT = ('.', ',', ')', '-', ':', ';', '?', '!')


# Функція по заміні знаків пунктуації
def replace_unit(text_in):
    for i in CONTAINER_UNIT:
        text_in = text_in.replace(i, '')
    return text_in


# Функція по заміні слів у реченні
def replace_word(z, x, y):
    return z.replace(x, y)


if __name__ == '__main__':
    # ввод предложения для обработки
    input_text = input(
        'Введите любой текст, где есть пробелы, запятые и много разного), не скупитесь на знаки .,-:;?!) \n'
    )
    find_word = input('Какое слово хотите заменить?\n')
    print(f'Ваше слово {find_word} находится на позиции: {input_text.find(find_word)}!')
    rep_word = input('На какое слово хотите заменить?\n')

    # выполняется замена слова
    final_text = replace_word(input_text, find_word, rep_word)

    # уведомления пользователя о выводе
    print('Мы получили вот такой результат:')
    print(replace_unit(final_text).rstrip().lower())

    # дані для перевірки функціональності програми
    # 1 HelLo, mY nAmE iS KyRyLo! I aM PrograMMing on C++) WhAt abOuT yoU? :)
    # 2 C++
    # 3 Python
