input_text = input('Введите любой текст, где есть пробелы, запятые и много разного), не скупитесь на знаки .,-:;?!) \n') # ввод предложения для обработки
# input_text = 'HelLo,.- mY nAmE iS: YuRii;! I. aM PrograMMing on C++) WhAt abOuT yoU? :)  ' # строка для теста, нужно просто раскоментить 3 строки, это первая

input_text_ed = input_text.lower() # превращение предложения в нижний регистр
input_text_ed = input_text_ed.replace('.', '') # Удаление точек в предложении
input_text_ed = input_text_ed.replace(',', '') # Удаление запятых в предложении
input_text_ed = input_text_ed.replace(')', '') # Удаление скобок в предложении
input_text_ed = input_text_ed.replace('-', '') # Удаление тире в предложении
input_text_ed = input_text_ed.replace(':', '') # Удаление двоеточия в предложении
input_text_ed = input_text_ed.replace(';', '') # Удаление точек с запятыми в предложении
input_text_ed = input_text_ed.replace('?', '') # Удаление знаков вопроса в предложении
input_text_ed = input_text_ed.replace('!', '') # Удаление знаков восклицания в предложении

find_word = input('Какое слово хотите заменить?\n') # какое слово надо заменить

#find_word = 'C++' # строка для теста, нужно просто раскоментить, это вторая

print(f'Ваше слово {find_word} находится на позиции: {input_text.find(find_word)}!') # вывод позиции слова в первоначальной формулировке

find_word_ed = find_word.lower() # это нужно, чтобы менять слово уже в измененном тексте

rep_word = input('На какое слово хотите заменить?\n') # на какое слово хотите заменить

# rep_word = 'Python' # для теста # строка для теста, нужно просто раскоментить, это крайняя

final_text = input_text_ed.replace(find_word_ed, rep_word) # выполняется замена слова

print(f'Мы получили вот такой результат:') # вывод результата
print(final_text.rstrip()) # вывод результата с удалением справа пробелов
