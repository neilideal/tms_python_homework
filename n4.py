import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4/3) * math.pi * self.radius**3

    def get_square(self):
        return 4 * math.pi * self.radius**2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.center[0])**2 + (y - self.center[1])**2 + (z - self.center[2])**2)
        return distance <= self.radius

def main():
    sphere = Sphere()
    while True:
        print("\nВыберите действие:")
        print("1. Установить радиус")
        print("2. Установить центр")
        print("3. Получить объем")
        print("4. Получить площадь")
        print("5. Получить радиус")
        print("6. Получить центр")
        print("7. Проверить, находится ли точка внутри сферы")
        print("8. Выход")
        choice = input("Ваш выбор: ")
        if choice == '8':
            break
        elif choice == '1':
            radius = float(input("Введите радиус: "))
            sphere.set_radius(radius)
        elif choice == '2':
            x = float(input("Введите координату x: "))
            y = float(input("Введите координату y: "))
            z = float(input("Введите координату z: "))
            sphere.set_center(x, y, z)
        elif choice == '3':
            print(f"Объем: {sphere.get_volume()}")
        elif choice == '4':
            print(f"Площадь: {sphere.get_square()}")
        elif choice == '5':
            print(f"Радиус: {sphere.get_radius()}")
        elif choice == '6':
            print(f"Центр: {sphere.get_center()}")
        elif choice == '7':
            x = float(input("Введите координату x: "))
            y = float(input("Введите координату y: "))
            z = float(input("Введите координату z: "))
            if sphere.is_point_inside(x, y, z):
                print("Точка находится внутри сферы")
            else:
                print("Точка находится вне сферы")
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()