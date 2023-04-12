from time import sleep
from random import randint, choices


# об`являємо клас
class Cat:
    # конструктор класса или метод инициализации
    # вызывается автоматически при создании объекта этого класса
    def __init__(
            self, name: str, sex: str, age: int,
            poroda: str, myau_min: int, play_min: int, pr_food: set
    ):
        """
        Рождение объекта класса/конструктор/инициализация
        :param name:
        """
        self.name = name
        self.sex = sex
        self.age = age
        self.poroda = poroda
        self.myau_min = myau_min
        self.play_min = play_min
        self.pr_food = pr_food
        self.cat_wont_sleep = True
        self.cat_walk = False
        self.hungry = False

    def __str__(self) -> str:
        return f'{self.poroda.title()}, {self.age} років за ім`ям {self.name}'

    def myau(self):
        print(f'{self.name} Мявкає!')

    def playmin(self):
        if self.play_min == 0:
            print(f'{self.name} Зовсім не погралася')
            cat.playmin()
        else:
            print(f'{self.name} грає {self.play_min} хвилин!')
            if self.play_min > 10:
                print('Можемо розслабитись')
                sleep(self.play_min)
                self.cat_wont_sleep = False
                self.hungry = True
                self.cat_walk = False
            else:
                print('Знову потрібно з котом погратись')
            self.myau()
            print('Мявчить, тому що все гуд')
        print(f'{self.name} зголодніла, завжди готова поїсти')

    def sleeptime():
        i = randint(0, 20)
        if i == 0:
            print('Кішка не виспалась')
            self.cat_wont_sleep = False
        self.cat_wont_sleep = True

    def myaumin(self):
        if self.myau_min == 0:
            print(f'{self.name} щось вона давно не мявкала')
        else:
            print(f'{self.name} знову мявкає вже {self.myau_min} хвилин!')
            print('Мявчить, значить все гуд!')
        print(f'{self.name} зголодніла')
        self.hungry = True

    def eat(self, suggested_food: str):
        if suggested_food in self.pr_food:
            print(f'{self.name} кушает {suggested_food}')
            self.hungry = False
        else:
            print(f'{self.name} предложили {suggested_food}, но мы такого не едим')


if __name__ == '__main__':
    Kisa = Cat('Кіса', 'ж', 1, 'Шотландка', randint(0, 3), randint(0, 20), {'риба', 'м`ясо', 'корм'})
    Nyusha = Cat('Нюша', 'ж', 3, 'Балинезійська', randint(0, 3), randint(0, 20), {'корм', 'солодощі', 'супродукти'})
    Belka = Cat('Білка', 'ж', 9, 'Бенгальська', randint(0, 3), randint(0, 20), {'корм', 'кістки', 'суп'})
    Lotos = Cat('Лотос', 'м', 8, 'Бомбейська', randint(0, 3), randint(0, 20), {'супродукти', 'каша', 'кисломолочка'})
    Snow = Cat('Сноу', 'м', 6, 'Бразильська ', randint(0, 3), randint(0, 20), {'кисломолочка', 'яйця', 'каша'})
    Night = Cat('Найт', 'м', 5, 'БРагамаффин', randint(0, 3), randint(0, 20), {'мясо', 'каша', 'сир', 'яйця'})

    po_food = ['риба', 'м`ясо', 'корм', 'кістки', 'супродукти', 'кисломолочка', 'борщ', 'каша', 'яйця']
    hungry_сats = list()
    for cat in [Kisa, Nyusha, Belka, Lotos, Snow, Night]:
        print(f'Звичайний день, кота на ім`я {cat}:')
        cat.myau()
        cat.myaumin()
        cat.playmin()
        for food in choices(po_food, k=2):
            cat.eat(food)
        if cat.hungry:
            hungry_сats.append(cat)

    if hungry_сats:
        print(f'Найдены {len(hungry_сats)} голодная(ые) собака(и), срочно покормите их!')
        print('Вот их имена:', ', '.join([Cat.name for Cat in hungry_сats]))
