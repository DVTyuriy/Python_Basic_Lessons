# блок обробки привітання
# Список ключів
Hello_word_1 = """ привіт,
 хай),
 доброго дня,
 хеллоу,"""

Enter_word = 's'
while Enter_word.lower() not in Hello_word_1:
    Enter_word = ' ' + input('Давай мо привітаємось, щоб почати спілкування: \n') + ','
    # порівнюємо відповідь з базою
    if Enter_word.lower() not in Hello_word_1:
        print('Я тебе не розумію, давай спробуємо ще')
print('Доброго вечора, я бот з України!')

# блок основної розмови
# відповіді у разі успішного ввода від юзера
ans_1 = 'Вчусь програмувати на Python!'
ans_2 = 'Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал "Американські боги", він просто бомба!'
ans_3 = "Побачимось у мережі, I'll be back."

# цикл обробки відповідей
while True:
    Enter_word = input().lower()
    # пошук в відповіді ключових слів блок 1
    if 'як справи?' in Enter_word or 'що робиш?' in Enter_word or 'чим займаєшся?' in Enter_word or 'чим зайнятий?' in Enter_word:
        print(ans_1)
    # пошук в відповіді ключових слів блок 2
    elif Enter_word.find('серіал') >= 0:
        print(ans_2)
    elif Enter_word.find('фільм') >= 0:
        print(ans_2)
    elif Enter_word.find('кіно') >= 0:
        print(ans_2)
    # пошук в відповіді ключових слів блок 3
    elif Enter_word.find('бувай') >= 0:
        print(ans_3)
        break
    elif Enter_word.find('надобраніч') >= 0:
        print(ans_3)
        break
    elif Enter_word.find('гудбай') >= 0:
        print(ans_3)
        break
    elif Enter_word.find('до зустрічі') >= 0:
        print(ans_3)
        break
    else:
        print('Ой, лишенько, я тебе не зрозумів. Ключових слів не знайдено')
