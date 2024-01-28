class Math:
    @staticmethod
    def addition(x, y):
        try:
            result = x + y
            print(f"Результат сложения: {result}")
            return result
        except TypeError:
            print(f"Ошибка: типы данных несовместимы для сложения!")

    @staticmethod
    def subtraction(x, y):
        try:
            result = x - y
            print(f"Результат вычитания: {result}")
            return result
        except TypeError:
            print(f"Ошибка: типы данных несовместимы для вычитания!")

    @staticmethod
    def multiplication(x, y):
        try:
            result = x * y
            print(f"Результат умножения: {result}")
            return result
        except TypeError:
            print(f"Ошибка: типы данных несовместимы для умножения!")

    @staticmethod
    def division(x, y):
        try:
            if y == 0:
                raise ZeroDivisionError(f"Ошибка: деление на ноль!")
            else:
                result = x / y
                print(f"Результат деления: {result}")
                return result
        except TypeError:
            print(f"Ошибка: типы данных несовместимы для деления!")

def main():
    math = Math()
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")
        choice = input("Ваш выбор: ")
        if choice == '5':
            break
        try:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            if choice == '1':
                math.addition(x, y)
            elif choice == '2':
                math.subtraction(x, y)
            elif choice == '3':
                math.multiplication(x, y)
            elif choice == '4':
                math.division(x, y)
            else:
                print("Неверный выбор. Попробуйте еще раз.")
        except ValueError:
            print("Ошибка: введено не числовое значение!")

if __name__ == "__main__":
    main()
