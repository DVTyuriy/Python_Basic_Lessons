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

# цикл обробки відпопідей
while True:
    Enter_word = input().lower()

    # пошук в відповіді ключових слів
    if Enter_word.find('як справи?') >= 0:
        print(ans_1)
    elif Enter_word.find('що робиш?') >= 0:
        print(ans_1)
    elif Enter_word.find('чим займаєшся?') >= 0:
        print(ans_1)
    elif Enter_word.find('чим зайнятий?') >= 0:
        print(ans_1)

    elif Enter_word.find('серіал') >= 0:
        print(ans_2)
    elif Enter_word.find('фільм') >= 0:
        print(ans_2)
    elif Enter_word.find('кіно') >= 0:
        print(ans_2)

    elif Enter_word.find('бувай') >= 0:
        print(ans_3)
        break
    elif Enter_word.find('надобраніч') >= 0:
        print(ans_3)
        break
    elif Enter_word.find('Гудбай') >= 0:
        print(ans_3)
        break
    elif Enter_word.find('До зустрічі') >= 0:
        print(ans_3)
        break
    else:
        print('Ой, лишенько, я тебе не зрозумів. Ключових слів не знайдено')
