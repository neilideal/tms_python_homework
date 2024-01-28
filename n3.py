class Car:
    TYPES = ["седан", "хэтчбек", "кроссовер", "внедорожник", "купе", "кабриолет", "минивэн", "пикап", "лимузин", "универсал"]
    COLORS = ["белый", "черный", "серый", "серебристый", "синий", "красный", "зеленый", "оранжевый", "бежевый", "фиолетовый"]

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведён")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска установлен на {self.year}")

    def set_type(self, type):
        self.type = type
        print(f"Тип установлен на {self.type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет установлен на {self.color}")

def main():
    car = Car("черный", "седан", 2020)
    while True:
        print("\nВыберите действие:")
        print("1. Завести автомобиль")
        print("2. Заглушить автомобиль")
        print("3. Установить год выпуска")
        print("4. Установить тип")
        print("5. Установить цвет")
        print("6. Выход")
        choice = input("Ваш выбор: ")
        if choice == '6':
            break
        elif choice == '1':
            car.start()
        elif choice == '2':
            car.stop()
        elif choice == '3':
            year = int(input("Введите год выпуска: "))
            car.set_year(year)
        elif choice == '4':
            print("Доступные типы: ")
            for i, type in enumerate(Car.TYPES, 1):
                print(f"{i}. {type}")
            type_index = int(input("Введите номер выбранного типа: ")) - 1
            car.set_type(Car.TYPES[type_index])
        elif choice == '5':
            print("Доступные цвета: ")
            for i, color in enumerate(Car.COLORS, 1):
                print(f"{i}. {color}")
            color_index = int(input("Введите номер выбранного цвета: ")) - 1
            car.set_color(Car.COLORS[color_index])
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
