from animal import Animal
from dog import Dog
from hen import Hen
from cow import Cow
from cat import Cat
from random import randint, choices


if __name__ == '__main__':
    # Додаємо обект та виконуємо над ним дії
    a = Animal('Чупакабра', {'???'}, -1)
    print(a, type(a))
    a.say()
    a.eat('печенька')
    a.treat()
    # Додаємо обекти
    farm_animals = [
        Dog('Напас', {'мясо', 'сало', 'борщ'}, 14),
        Hen('Ряба', {"пшено", "крупа", "вода"}, 2),
        Cow('Бурёнка', {"трава", "сено"}, 5),
        Cat('Нюша', {'корм', 'солодощі', 'супродукти'}, 3)
    ]
    # пример полиморфизма - одинаковые названия функций, но разные классы и разная логика выполнения.
    food_to_offer = ['мясо', 'сало', 'борщ', "пшено", "крупа", "вода", "трава", "сено"]
    what_we_lost = list()
    what_we_get = list()
    hungrys = list()
    not_hungrys = list()
    # Перебираємо обекти та для кожного виконуємо наступні дії
    for animal in farm_animals:
        print('\n', animal, type(animal))
        # Викликаємо функцію, що вимовляє тварина
        animal.say()
        # Цикл пребираємо їжу для тварин
        for food in choices(food_to_offer, k=3):
            animal.eat(food)
            what_we_lost.append(food)
        what_we_get.append(animal.treat(randint(0, 5)))
    print()
    # Додаємо обекти
    farm_animals.append(a)
    farm_animals.append('Оса')
    farm_animals.append(5)
    farm_animals.append([3, 4, 'Шершень'])
    # цикл перебору тварин, чи ситі вони та чи належать вони до ферми
    for animal in farm_animals:
        # if type(5) == int
        # if type(animal) == Dog
        # то же самое, что и выше, но рекомендуется сравнивать типы именно через isinstance
        if isinstance(animal, Animal):
            print(f'Найден представитель типа данных Animal: {animal}')
            if animal.hungry:
                print(f"На вашей ферме голодное животное! {animal}")
                hungrys.append(animal)
            else:
                not_hungrys.append(animal)
        else:
            print(f"{animal} не с нашей фермы.")
    print()
    # Що давали тваринам, та що тварини віддали нам
    print(f'Ухаживая за животными, мы потеряли: {what_we_lost}')
    print(f'Ухаживая за животными, мы получили: {what_we_get}')
    # виводимо на екран які тварини стали ситі, а які голодні
    if hungrys:
        print(f'\n{len(hungrys)} тварин залишилось голодними')
        print('Ось вони, бешкетники:', ', '.join([Animal.name for Animal in hungrys]), 'які голодні')
        print('А ось довольні морди:', ', '.join([Animal.name for Animal in not_hungrys]), 'які наїлися')
