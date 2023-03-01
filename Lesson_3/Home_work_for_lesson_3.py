# ввод предложения для обработки
input_text = input('Введите любой текст, где есть пробелы, запятые и много разного), не скупитесь на знаки .,-:;?!) \n')

# строка для теста, нужно просто раскоментить 3 строки, это первая
# input_text = 'HelLo, mY nAmE iS KyRyLo! I aM PrograMMing on C++) WhAt abOuT yoU? :)'

# какое слово надо заменить
find_word = input('Какое слово хотите заменить?\n')

# строка для теста, нужно просто раскоментить, это вторая
# find_word = 'C++'

# вывод позиции слова в первоначальной формулировке
print(f'Ваше слово {find_word} находится на позиции: {input_text.find(find_word)}!')

# на какое слово хотите заменить
rep_word = input('На какое слово хотите заменить?\n')

# строка для теста, нужно просто раскоментить, это крайняя
# rep_word = 'Python'

# выполняется замена слова
final_text = input_text.replace(find_word, rep_word)

# Удаление знаков .,)-:;?! в предложении
final_text = final_text.replace('.', '')
final_text = final_text.replace(',', '')
final_text = final_text.replace(')', '')
final_text = final_text.replace('-', '')
final_text = final_text.replace(':', '')
final_text = final_text.replace(';', '')
final_text = final_text.replace('?', '')
final_text = final_text.replace('!', '')

# превращение предложения в нижний регистр
final_text = final_text.lower()

# уведомления пользователя о выводе
print('Мы получили вот такой результат:')
print(final_text.rstrip())
