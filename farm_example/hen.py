from animal import Animal


class Hen(Animal):
    # конструктор класа або метода ініціалізації
    def __init__(self, name: str, preferred_food: set, age: int):
        """
        передаємо та переопреділяємо параметри обекта
        :param name: параметр обекта їмя
        :param preferred_food: параметр обекта що їсть
        :param age: параметр обекта скільки років
        """
        super().__init__(name, preferred_food, age)

        # Переопреділяємо параметр
        self.say_word = "Кудах-кудах"
        self.animal_type = "Курица"

    # Функція догляду для цього класу
    def treat(self, hours: int = 1) -> str:
        print(f"Вы ухаживаете за {self.name} {hours} часов.")
        return "Куриные яйца"
