from time import sleep
from random import randint, choices


# об`являємо клас
class Cat:
    # конструктор класа або метода ініціалізації
    def __init__(
            self, name: str, sex: str, age: int,
            poroda: str, myau_min: int, play_min: int, pr_food: set
    ):
        """
        Створення обекта
        :param name: імя
        :param sex: пол
        :param age: вік
        :param poroda: порода
        :param myau_min: може мяукати стільки часу, вибирається рандомно
        :param play_min: скільки грає, вибирається рандомно
        :param pr_food: їда, яку полюбляє
        """
        self.name = name
        self.sex = sex
        self.age = age
        self.poroda = poroda
        self.myau_min = myau_min
        self.play_min = play_min
        self.pr_food = pr_food
        self.hungry = True

    def __str__(self) -> str:
        """
        Виводить інформацію про обект
        :return: строку з параметрами
        """
        return f'{self.poroda.title()}, {self.age} років за ім`ям {self.name}'

    def myau(self):
        """
        Виводить строку з обектом
        """
        print(f'{self.name} Мурлика, значить все добре !')

    def playmin(self):
        """
        Виводить строку про гру обекта в залежності від рандомного числа
        """
        if self.play_min == 0:
            print(f'{self.name} Зовсім не погралася')
        else:
            print(f'{self.name} грає {self.play_min} хвилин!')
            if self.play_min > 10:
                print('Можемо розслабитись')
            else:
                print(f'Мало погралась, тільки {self.play_min} хвилин!')
            self.myau()

    def sleeptime(self):
        """
        Виводить строку про сон обекта в залежності від рандомного числа
        """
        i = randint(0, 20)
        if i == 0:
            print('Кішка не спала')
        else:
            print(f'Кішка поспала {i} хвилин')
            self.myau()
            print(f'{self.name} зголодніла, завжди готова поїсти після {i} хвилин сну')

    def myaumin(self):
        """
        Виводить строку про мяукання обекта в залежності від рандомного числа
        """
        if self.myau_min == 0:
            print(f'{self.name} щось вона не мявкає')
        else:
            print(f'{self.name} знову мявкає вже {self.myau_min} хвилин!')
            print('Мявчить, значить все гуд!')

    def eat(self, suggested_food: str):
        """
        Функція оброблє чи підійшла їжа обекту
        :param suggested_food: їжа
        :return: повертає для "hungry" "False" якщо обект поїв
        """
        if suggested_food in self.pr_food:
            print(f'{self.name} їсть {suggested_food}')
            self.hungry = False
        else:
            print(f'Положили {suggested_food} для {self.name}, гарчить, не їсть')


if __name__ == '__main__':
    # Формуємо базу обектів
    Kisa = Cat('Кіса', 'ж', 1, 'Шотландка', randint(0, 3), randint(0, 20), {'риба', 'м`ясо', 'корм'})
    Nyusha = Cat('Нюша', 'ж', 3, 'Балинезійська', randint(0, 3), randint(0, 20), {'корм', 'солодощі', 'супродукти'})
    Belka = Cat('Білка', 'ж', 9, 'Бенгальська', randint(0, 3), randint(0, 20), {'корм', 'кістки', 'суп'})
    Lotos = Cat('Лотос', 'м', 8, 'Бомбейська', randint(0, 3), randint(0, 20), {'супродукти', 'каша', 'кисломолочка'})
    Snow = Cat('Сноу', 'м', 6, 'Бразильська ', randint(0, 3), randint(0, 20), {'кисломолочка', 'яйця', 'каша'})
    Night = Cat('Найт', 'м', 5, 'БРагамаффин', randint(0, 3), randint(0, 20), {'мясо', 'каша', 'сир', 'яйця'})
    # Формуємо базу продуктів, які будемо пропонувати
    po_food = ['риба', 'м`ясо', 'корм', 'кістки', 'супродукти', 'кисломолочка', 'борщ', 'каша', 'яйця']
    hungry_cats = list()
    # Цикл повсякденності для кожного обекта
    for cat in [Kisa, Nyusha, Belka, Lotos, Snow, Night]:
        print(f'\n\nЗвичайний день кота породи {cat}:')
        cat.myaumin()
        cat.playmin()
        cat.sleeptime()
        sleep(cat.play_min)
        # Цикл в якому ми пропонуємо їжу
        for food in choices(po_food, k=2):
            cat.eat(food)
        # Якщо обект нічого не зїв
        if cat.hungry:
            print('Кіса залишилась голодна')
            hungry_cats.append(cat)
    # Формуємо кількість і список обектів які залишились голодними
    if hungry_cats:
        print(f'\n\n{len(hungry_cats)} кіт/котів/а залишилось голодними')
        print('Ось вони, бешкетники:', ', '.join([Cat.name for Cat in hungry_cats]))
