import math

# константа зі знаків пунктуації
CONTAINER_UNIT = ('.', ',', ')', '-', ':', ';', '?', '!')


def input_num(i):
    try:
        float(i)
        return i

    except Exception:
        print('Ні, мені потрібне саме тільки число, яке буде довжиною сторони трикутника')



# def input_num(comment):
#     while True:
#         try:
#             v = float(input(comment))
#             return v
#         except Exception:
#             print('Ні, мені потрібне саме тільки число, яке буде довжиною сторони трикутника')


def check_triangle(z: float, x: float, y: float):
    if z + x > y and z + y > x and x + y > z:
        return True
    else:
        return False


def sum(z1: float, x1: float, y1: float):
    return z1 + x1 + y1


def square(qs: float, zs: float, xs: float, ys: float):
    half_p = qs / 2
    return math.sqrt(half_p * (half_p - zs) * (half_p - xs) * (half_p - ys))


if __name__ == '__main__':

    a = input('Введіть довжину сторони "A" трикутника в см.: ')
    a = input_num(a)
    b = input('Введіть довжину сторони "B" трикутника в см.: ')
    b = input_num(b)
    c = input('Введіть довжину сторони "C" трикутника в см.: ')
    c = input_num(c)

    # b = input_num('Введіть довжину сторони "B" трикутника в см.: ')
    # c = input_num('Введіть довжину сторони "C" трикутника в см.: ')
    print(check_triangle(a, b, c))
    print(f'Периметр трикутника становить: {sum(a, b, c)} см.')
    p = sum(a, b, c)
    print(f'Площа трикутника становить: {square(p, a, b, c):.2f} см².')

