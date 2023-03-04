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

# блок розмови про справи
# відповідь у разі успішного ввода від юзера
ans_1 = 'Вчусь програмувати на Python!'
x = 1
while x == 1:
    Enter_word = input().lower()
    # пошук в відповіді ключові слова
    if Enter_word.find('як справи?') >= 0:
        print(ans_1)
        x += 1
    elif Enter_word.find('що робиш?') >= 0:
        print(ans_1)
        x += 1
    elif Enter_word.find('чим займаєшся?') >= 0:
        print(ans_1)
        x += 1
    elif Enter_word.find('чим зайнятий?') >= 0:
        print(ans_1)
        x += 1
    else:
        print('Ой, лишенько, я тебе не зрозумів')

# блок розмови про серіали
# відповідь у разі успішного ввода від юзера
ans_1 = 'Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал "Американські боги", він просто бомба!'
i = 0
while True:
    Enter_word = input().lower()
    # перевірка кількості повторів
    if i == 2:
        break
    elif Enter_word.find('серіал') >= 0:
        print(ans_1)
        i += 1
    elif Enter_word.find('фільм') >= 0:
        print(ans_1)
        i += 1
    elif Enter_word.find('кіно') >= 0:
        print(ans_1)
        i += 1
    else:
        print('Та годі тобі, давай щось про серіали чи просто про кіно')

# фінальний блок, прощальний)
# відповідь у разі успішного ввода від юзера
ans_1 = "Побачимось у мережі, I'll be back."
while True:
    if Enter_word.find('бувай') >= 0:
        print(ans_1)
        break
    elif Enter_word.find('надобраніч') >= 0:
        print(ans_1)
        break
    elif Enter_word.find('Гудбай') >= 0:
        print(ans_1)
        break
    elif Enter_word.find('До зустрічі') >= 0:
        print(ans_1)
        break
    else:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :( Давай будемо завершувати розмову')
        Enter_word = input().lower()
