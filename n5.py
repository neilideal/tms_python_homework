class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        if self == s * (len(self) // len(s)):
            return True
        return False

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]

def main():
    s = SuperStr(input("Введите строку: "))
    while True:
        print("\nВыберите действие:")
        print("1. Проверить, является ли строка повторением другой строки")
        print("2. Проверить, является ли строка палиндромом")
        print("3. Изменить строку")
        print("4. Выход")
        choice = input("Ваш выбор: ")
        if choice == '4':
            break
        elif choice == '1':
            t = input("Введите другую строку: ")
            if s.is_repeatance(t):
                print("Строка является повторением другой строки")
            else:
                print("Строка не является повторением другой строки")
        elif choice == '2':
            if s.is_palindrom():
                print("Строка является палиндромом")
            else:
                print("Строка не является палиндромом")
        elif choice == '3':
            s = SuperStr(input("Введите новую строку: "))
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()