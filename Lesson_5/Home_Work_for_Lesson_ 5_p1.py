Sum_num = 0
i = 0
# виконуємо цикл вводу та обчислення
while True:
    Enter_num = input('Введіть число для обчислення суми чисел чи введіть "sum" для отримання результату\n')

    # Виконується вихід з циклу, якщо було введено sum
    if 'sum' in Enter_num.lower():
        print('Кількість чисел для обчислення становить: ', i)
        print('Успіх, сума всіх чисел становить', Sum_num)
        break

    # перевіряємо на правильність вводу, та сумуємо числа
    try:
        float(Enter_num)
        Sum_num += float(Enter_num)
        i += 1
        print('Число додано до обчислювання')
        # якщо не число, то повідомляємо про помилку
    except Exception:
        print('Ох, дідько, щось я перестав тебе розуміти, давай знову спробуємо')
