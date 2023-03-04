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
      print()


x = True
while x == True:
    Enter_word = input('Доброго вечора, я бот з України!\n').lower()
    # пошук в відповіді ключові слова
    if Enter_word.find('як справи?') >= 0:
       print('Вчусь програмувати на Python!')
       x = False
    elif Enter_word.find('що робиш?') >= 0:
       print('Вчусь програмувати на Python!')
       x = False
    elif Enter_word.find('чим займаєшся?') >= 0:
       print('Вчусь програмувати на Python!')
       x = False
    elif Enter_word.find('чим зайнятий?') >= 0:
       print('Вчусь програмувати на Python!')
       x = False
    else:
        print('Я тебе не зрозумів')
i = 0

while True:
    Enter_word = input().lower()
    if i == 2:
        break
    elif Enter_word.find('серіал') >= 0:
       print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал "Американські боги", він просто бомба!')
       i += 1
    elif Enter_word.find('фільм') >= 0:
       print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал "Американські боги", він просто бомба!')
       i += 1
    elif Enter_word.find('кіно') >= 0:
        print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал "Американські боги", він просто бомба!')
        i += 1
    else:
        print('Та годі тобі, давай щось про серіали чи просто про кіно')

while True:
    if Enter_word.find('бувай') >= 0:
       print("Побачимось у мережі, I'll be back.")
       break
    elif Enter_word.find('надобраніч') >= 0:
       print("Побачимось у мережі, I'll be back.")
       break
    elif Enter_word.find('Гудбай') >= 0:
        print("Побачимось у мережі, I'll be back.")
        break
    elif Enter_word.find('До зустрічі') >= 0:
        print("Побачимось у мережі, I'll be back.")
        break
    else:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
