import re

def sum_numbers_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Содержимое файла: {content}")
        numbers = re.findall(r'\d+', content)
        print("Слагаемые: " + ' + '.join(numbers))
        return sum(int(num) for num in numbers)

# Пример использования:
print("Сумма: ", sum_numbers_in_file('numbers.txt'))
