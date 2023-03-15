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
    # інпут текста для обробки
    input_text = input(
        'Введіть, будь ласка, текст де буде дуже багато різних непотрібних знаків, таких як .,-:;?!) \n'
    )
    # виконуємо дії з введеним текстом
    find_word = input('Яке слово потрібно замінити?\n')
    print(f'Ваше слово {find_word} знаходиться на позиції: {input_text.find(find_word)}!')
    rep_word = input('На яке потрібно замінити?\n')

    # виконуємо заміну слова
    final_text = replace_word(input_text, find_word, rep_word)

    # виводимо результат
    print('Після кропіткої роботи, ми отримали такий результат:')
    print(replace_unit(final_text).rstrip().lower())

    # дані для перевірки функціональності програми
    # 1 HelLo, mY nAmE iS KyRyLo! I aM PrograMMing on C++) WhAt abOuT yoU? :)
    # 2 C++
    # 3 Python
