from time import sleep
from random import randint, choices

# об`являємо клас
class Cat:
    # конструктор класса или метод инициализации
    # вызывается автоматически при создании объекта этого класса
    def __init__(
            self, name: str, gender: str, age: int,
            poroda: str, myau_min: int, preferred_food: set
    ):
        """
        Рождение объекта класса/конструктор/инициализация
        :param name:
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.poroda = poroda
        self.myau_min = myau_min
        self.preferred_food = preferred_food
        self.cat_wont_sleep = False 
        self.cat_walk = False
        self.hungry = False

    def __str__(self) -> str:
        return f'{self.poroda.title()}, {self.age} лет по кличке {self.name}'

    def bark(self):
        print(f'{self.name} Мяукає!')

    def play(self):
        if self.play_hours == 0:
            print(f'{self.name} не гуляє')
        else:
            print(f'{self.name} играет {self.play_hours} часов!')
            print('Ждемо...')
            # sleep(self.play_hours)
            self.bark()
            print('Гавкает потому что довольна!')
        print(f'{self.name} проголодалась')
        self.hungry = True

    def eat(self, suggested_food: str):
        if suggested_food in self.preferred_food:
            print(f'{self.name} кушает {suggested_food}')
            self.hungry = False
        else:
            print(f'{self.name} предложили {suggested_food}, но мы такого не едим')


if __name__ == '__main__':
    kisa= Cat('Кіса', 'ж', 4, 'Шотландка', randint(2, 6), {'риба', 'м`ясо'})
    Nyusha = Cat('', 'M', 5, 'йоркский терьер', 0, {'корм', 'яблоки'})
    napas = Cat('Напас', 'M', 14, 'такса', 1, {'корм', 'сало', 'борщ'})
    jessy = Cat('Джесси', 'Ж', 9, 'канекорса', 4, {'мясо', 'каша'})

    potential_food = ['рыба', 'мясо', 'корм', 'яблоки', 'сало', 'борщ', 'каша']
    print(bobik, type(bobik))
    print(rocky, type(rocky))
    hungry_Cats = list()
    for Cat in [bobik, rocky, napas, jessy]:
        print('=' * 20, f'\nОбычный день {Cat}:')
        Cat.bark()
        Cat.play()
        # choices(list, k=3) k - сколько раз выбрать случайный элемент
        for food in choices(potential_food, k=2):
            Cat.eat(food)
        if Cat.hungry:
            hungry_Cats.append(Cat)

    if hungry_Cats:
        print(f'Найдены {len(hungry_Cats)} голодная(ые) собака(и), срочно покормите их!')
        print('Вот их имена:', ', '.join([Cat.name for Cat in hungry_Cats]))