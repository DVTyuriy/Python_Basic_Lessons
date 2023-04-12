class Animal:
    # initialization
    # вызывается автоматически при создании объекта класса
    # Animal.__init__() то же самое, что Animal()
    def __init__(self, name: str, preferred_food: set, age: int):
        """
        Передаємо та опреділяємо параметри обекта
        :param name: параметр обекта їмя
        :param preferred_food: параметр обекта що їсть
        :param age: параметр обекта скільки років
        """
        self.name = name
        self.preferred_food = preferred_food
        self.age = age
        self.say_word = "???"
        self.animal_type = "Животное"
        self.hungry = True

        # return self представьте что оно здесь так

    def __str__(self):
        return f"{self.animal_type} по имени {self.name}, {self.age} лет."

    def eat(self, suggested_food: str):
        """
        Функція оброблє чи підійшла їжа обекту
        :param suggested_food: їжа
        :return: повертає для "hungry" "False" якщо обект поїв
        """
        if suggested_food in self.preferred_food:
            print(f'{self.name} їсть {suggested_food}')
            self.hungry = False
        else:
            print(f'Положили {suggested_food} для {self.name}, гарчить, не їсть')

    def say(self):
        """
        Функція, яка обробляе що вимовляє кожна тварина
        """
        print(f"{self.name} говорит: {self.say_word}")

    def treat(self, hours: int = 1):
        """
        Функція яка обробляє та виводить на екран скільки ми доглядажємо за твариною
        :param hours: скільки доглядаємо за твариною, за замовчуванням 1 година
        """
        print(f"Вы ухаживаете за {self.name} {hours} час(ов)")
        if self.hungry:
            print(f"{self.name} голодное!")
