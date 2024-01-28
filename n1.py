class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"У вас газировка со вкусом: {self.flavor}"
        else:
            return "У вас обычная газировка"

def main():
    flavor = input("Введите вкус газировки или нажмите Enter для обычной газировки: ")
    soda = Soda(flavor)
    print(soda)

if __name__ == "__main__":
    main()