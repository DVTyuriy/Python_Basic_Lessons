import math

#-------------------------------------------------------------------------------------------------------
# Task #1
# Вхідні дані
    # градуси (або радіани)
# На виході:')
    # конвертована величина (градуси або радіани) округлена до 5 цифр після коми'

print('Task #1')

a = input('Enter gradus: ')

x = float(a) * math.pi / 180 # перевод в радианы

print(f'Radian: {round(x, 5)}')
print('----------End Task----------')

#-------------------------------------------------------------------------------------------------------
# Task #2
# Написати програму, що рахує абонплату за комунальним лічильником (наприклад, електроенергії або газу).
# Вхідні дані:
    # попередні показання
    # теперішні показання
    # тариф.
#На виході:
    # скільки потрібно сплатити, округлено до двох цифр після коми

print('Task #2')

l = input('Прошлые показания: ')
t = input('Актуальные показания: ')
tr = input('Тариф: ')

a = (float(t) - float(l)) * float(tr) # расчет стоимости коммуналки

print(f'Коммуналка составляет: {a:.2f}')
print('----------End Task----------')

#-------------------------------------------------------------------------------------------------------
#Task 3
# Написати програму, що рахує податок від надхождення на рахунок підприємця.
    # Вхідні дані:
        # розмір надходження
        # відсоток податка}
    # На виході:
        # скільки потрібно сплатити податку
        # скільки залишиться чистого прибутку
        # (обидва значення округлені до двох цифр після коми)

print('Task #3')

p = input('Приход: ')
pr = input('Налог: ')

t = float(p) * float(pr) / 100  # расчет налога
d = float(p) - t                # расчет чистого дохода

print(f'Доход: {d}')
print(f'Оплатить налог: {t}')
print(f'Дохoд: {d:.2f} Оплатить налог: {t:.2f}')
print('----------End Task----------')

#-------------------------------------------------------------------------------------------------------
# Task #4
# Написати програму що рахує витрати на паливо.
# Вхідні дані:
    # витрачання палива автомобілем за 100км
    # сьогоднішня ціна 1 л палива
    # скільки кілометрів треба здолати
# На виході:
    # скільки грошей на це піде, округлено до двох цифр після коми

print('Task #4')

o = input('Расход топлива на 100км: ')
i = input('Стоимость топлива за 1л.: ')
u = input('Сколько км надо проехать: ')

g = float(u) / 100 * float(o) * float(i) # расчет стоимости поездки

print(f'Сколько денег нужно на дорогу: {g:.2f}')
print('----------End Task----------')
