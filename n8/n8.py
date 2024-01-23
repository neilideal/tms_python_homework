import json
import csv
import re
import io

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def clean_data(data):
    for item in data:
        for key, value in item.items():
            if isinstance(value, str):
                # Удаление всех кавычек и скобок
                item[key] = re.sub('[\'"(){}\\[\\]]', '', value)
    return data

def validate_employee_data(employee_data):
    required_keys = ["name", "birthday", "height", "weight", "car", "languages"]
    return all(key in employee_data for key in required_keys)

def json_to_csv():
    json_file = 'employees.json'
    csv_file = 'employees.csv'
    with open(json_file, 'r') as jf:
        data = json.load(jf)
        data = clean_data(data)
        for item in data:
            item['languages'] = ', '.join(item['languages'])

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=data[0].keys(), quoting=csv.QUOTE_NONE, escapechar='\\')
    writer.writeheader()
    for row in data:
        writer.writerow(row)

    csv_data = buffer.getvalue()
    csv_data = csv_data.replace('\\', '')

    with open(csv_file, 'w', newline='') as cf:
        cf.write(csv_data)

def add_employee_to_json():
    employee_data = {}
    fields = ["name", "birthday", "height", "weight", "car", "languages"]
    for field in fields:
        if field == "languages":
            print("Введите языки программирования через запятую: ")
            languages = input().split(',')
            employee_data[field] = [lang.strip() for lang in languages]
        elif field == "car":
            print("Есть ли у сотрудника машина? (да/нет): ")
            car = input().lower()
            employee_data[field] = True if car == "да" else False
        else:
            print(f"Введите {field}: ")
            employee_data[field] = input()

    if not validate_employee_data(employee_data):
        print("Неверный формат данных о сотруднике.")
        return

    json_file = 'employees.json'
    with open(json_file, 'r+') as jf:
        data = json.load(jf)
        data.append(employee_data)
        jf.seek(0)
        json.dump(data, jf)

    # Автоматический запуск json_to_csv после добавления нового сотрудника
    json_to_csv()

def add_employee_to_csv():
    employee_data = {}
    fields = ["name", "birthday", "height", "weight", "car", "languages"]
    for field in fields:
        if field == "languages":
            print("Введите языки программирования через запятую: ")
            languages = input().split(', ')
            employee_data[field] = [lang.strip() for lang in languages]
        elif field == "car":
            print("Есть ли у сотрудника машина? (да/нет): ")
            car = input().lower()
            employee_data[field] = True if car == "да" else False
        else:
            print(f"Введите {field}: ")
            employee_data[field] = input()

    if not validate_employee_data(employee_data):
        print("Неверный формат данных о сотруднике.")
        return

    csv_file = 'employees.csv'
    with open(csv_file, 'a', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=employee_data.keys())
        writer.writerow(employee_data)

def get_employee_by_name(name):
    json_file = 'employees.json'
    with open(json_file, 'r') as jf:
        data = json.load(jf)
        for employee in data:
            if employee['name'] == name:
                return employee

def filter_by_language(language):
    json_file = 'employees.json'
    with open(json_file, 'r') as jf:
        data = json.load(jf)
        return [employee for employee in data if language in employee['languages']]

def average_height_by_year(year):
    json_file = 'employees.json'
    with open(json_file, 'r') as jf:
        data = json.load(jf)
        filtered_employees = [employee for employee in data if employee['birth_year'] < year]
        return sum(employee['height'] for employee in filtered_employees) / len(filtered_employees)

def interactive_menu():
    while True:
        print("Выберите действие:")
        print("1. Преобразовать JSON в CSV")
        print("2. Добавить сотрудника в JSON")
        print("3. Добавить сотрудника в CSV")
        print("4. Получить информацию о сотруднике по имени")
        print("5. Фильтровать сотрудников по языку программирования")
        print("6. Вычислить средний рост сотрудников по году рождения")
        print("7. Выйти из программы")
        choice = input("Ваш выбор: ").strip()
        if choice == '1':
            json_to_csv()
        elif choice == '2':
            add_employee_to_json()
        elif choice == '3':
            add_employee_to_csv()
        elif choice == '4':
            name = input("Введите имя сотрудника: ").strip()
            print(get_employee_by_name(name))
        elif choice == '5':
            language = input("Введите язык программирования: ").strip()
            print(filter_by_language(language))
        elif choice == '6':
            year = int(input("Введите год рождения: ").strip())
            print(average_height_by_year(year))
        elif choice == '7':
            break

interactive_menu()
