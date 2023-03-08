
for i in range(100):
    Enter_num = input('Введіть число для обчислення суми чисел чи введіть "sum" для отримання результату\n')
    if 'sum' in Enter_num.lower():
        print('Конграт, сума чисел становить')
        break
    try:
        float(Enter_num)
        x.append(Enter_num)
    except ValueError:
        print('Ох, дідько, щось я перестав тебе розуміти, давай знову спробуємо')






    Enter_num = input('Введіть число для обчислення суми чисел та потім введіть "sum" для отримання результату\n')

    if 'sum' in Enter_num.lower():
        break

    try:
        float(Enter_num)
        x.append(Enter_num)
        print('yes')
    except Exception:
        print('Ох, дідько, щось я перестав тебе розуміти, давай знову спробуємо')

print('Кількість чисел для вичисленні становить: ', len(x))

for i in len(x):
    Sum_num += x[i]

print('Сума становить: ', Sum_num)



    # if 'sum' in Enter_num.lower():1

    #     print('Конграт, сума чисел становить', Sum_num)
    #     break
    # elif Enter_num.isdigit():
    #     Sum_num = Sum_num + float(Enter_num)
    # else:
    #     print('Ох, дідько, щось я перестав тебе розуміти, давай знову спробуємо')