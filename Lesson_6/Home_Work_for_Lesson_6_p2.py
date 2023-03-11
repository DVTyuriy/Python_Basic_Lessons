# зчитуємо від користувача інформацію для обробки
input_word = input('Введіть текст, в якому потрібно видалити те, що в дужках, '
                   'або введіть "1" для перевірки фрази за замовчуванням\n')
if input_word == '1':
    input_word = 'Я не знав куди йти (втім не дивно), ' \
                 'тому пішов.. "вийде" Я не знав куди йти, тому (втімнедивно), пішов..'
    print(f'Ось фраза, яка буде перевірена:\n{input_word}')
print()

# переводимо введену інформацію в список для обробки
text_words = input_word.split()

# об`являємо змінні
res_word_a = list()
res_word_b = list()
res_word = list()
a = 0
b = 0

# добавляємо нуль до списку b, що б почати відлік у поточному списку
res_word_b.append(0)
# дізнаємось дліну списка, щоб перебрати та перевірити всі елементи
lenth_input = len(text_words)
# перевіряємо список на дужки та записуємо їх індекси (для кожної дужки окремо)
for i in range(lenth_input):
    # перевірка, якщо у нас в дужках одне слово
    if '(' in text_words[i] and ')' in text_words[i]:
        a = i
        res_word_a.append(a)
        b = i + 1
        res_word_b.append(b)
    elif '(' in text_words[i]:
        a = i
        res_word_a.append(a)
    elif ')' in text_words[i]:
        b = i + 1
        res_word_b.append(b)

# додаємо кінцевий індекс до списку а, що б додати потім кінцеві елементи
res_word_a.append(lenth_input)

# дізнаємось дліну списка отриманих індексів дужок
lenth_list = len(res_word_a)

# склеюємо отримані відрізки тексту без дужок
for i in range(lenth_list):
    res_word.extend(text_words[res_word_b[i]:res_word_a[i]])

# перетворюємо список в строку та виводимо результат
res_word_res = " ".join(res_word)
print(f'Ось, що ми отримали після клопіткої праці:\n{res_word_res}')
print()
if res_word_res == input_word:
    print('Ми дуже уважно перевірили, але тексту в дужках для його скорочення так і не знайшли')
