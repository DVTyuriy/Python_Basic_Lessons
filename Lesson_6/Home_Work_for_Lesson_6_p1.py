# зчитуємо від користувача інформацію для обробки
input_word = input('Введіть інформацію, яка може бути паліндромом, а я перевірю чи це саме так\n')

# переводимо введену інформацію в список для обробки
text_words = input_word.split()

# позбуваємося лишніх знаків пунктуації
stripped_words = list()
for word in text_words:
    stripped_words.append(word.strip('(),.;:'))

# об`єднуємо в набір символів
stripped_words = "".join(stripped_words).lower()

# розбиваємо набір символів та утворюємо список
list_unit = list()
for unit in stripped_words:
    list_unit.append(unit)

# Обертаемо список, щоб перший елемент став останнім, щоб потім порівняти
back_list_unit = list(reversed(list_unit))

# об`єднуємо кожний список в набір символів
list_unit = "".join(list_unit).lower()
back_list_unit = "".join(back_list_unit).lower()

# порівнюємо два набіра символів, та виводимо результат
if list_unit in back_list_unit:
    print('Мої вітання, таки введене являється паліндромом')
else:
    print('Мені дуже прикро, але це не є паліндромом')
