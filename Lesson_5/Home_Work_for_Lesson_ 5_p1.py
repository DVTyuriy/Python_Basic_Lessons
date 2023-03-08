Sum_num = 0
while True:
    Enter_num = input('Введіть число для обчислення суми чисел чи введіть "sum" для отримання результату\n')
    if 'sum' in Enter_num.lower():
        print('Конграт, сума чисел становить', Sum_num)
        break
    try:
        float(Enter_num)
        Sum_num = Sum_num + float(Enter_num)
    except Exception:
        print('Ох, дідько, щось я перестав тебе розуміти, давай знову спробуємо')

