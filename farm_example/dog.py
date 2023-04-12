from animal import Animal


class Dog(Animal):
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
        self.say_word = "Гав-гав!"
        self.animal_type = "Собака"

        # del self.name антипаттерн, противоречит принципу наследования

    # Функція догляду для цього класу
    def treat(self, hours: int = 1) -> str:
        print(f"Мы гуляем с {self.name} {hours} часов и у нас поднимается настроение.")
        return "Хорошее настроение"
