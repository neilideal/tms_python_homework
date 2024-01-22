def print_students_with_low_scores(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            name, score = line.rsplit(' ', 1)
            if int(score) < 3:
                print(name)

# Запуск функции
print_students_with_low_scores('students.txt')