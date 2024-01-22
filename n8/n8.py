import json
import csv
import re

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def json_to_csv():
    json_file = 'employees.json'
    csv_file = 'employees.csv'
    with open(json_file, 'r') as jf:
        data = json.load(jf)

    with open(csv_file, 'w', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def add_employee_to_json(employee_data):
    json_file = 'employees.json'
    with open(json_file, 'r+') as jf:
        data = json.load(jf)
        data.append(employee_data)
        jf.seek(0)
        json.dump(data, jf)

def add_employee_to_csv(employee_data):
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
        choice = input("Ваш выбор: ")
        if choice == '1':
            json_to_csv()
        elif choice == '2':
            employee_data = input("Введите данные о сотруднике в формате JSON: ")
            add_employee_to_json(json.loads(employee_data))
        elif choice == '3':
            employee_data = input("Введите данные о сотруднике в формате JSON: ")
            add_employee_to_csv(json.loads(employee_data))
        elif choice == '4':
            name = input("Введите имя сотрудника: ")
            print(get_employee_by_name(name))
        elif choice == '5':
            language = input("Введите язык программирования: ")
            print(filter_by_language(language))
        elif choice == '6':
            year = int(input("Введите год рождения: "))
            print(average_height_by_year(year))
        elif choice == '7':
            break