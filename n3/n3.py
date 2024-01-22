import re
from collections import Counter

def most_common_word_in_line(file_name):
    # Очистка файла output.txt перед началом работы
    open('output.txt', 'w').close()
    print("Файл output.txt был очищен")

    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Вывод текста input.txt без сервисных строк
    print("Текст input.txt без сервисных строк:")
    lines = [line for line in lines if not re.search(r'[\[\]:&]', line)]
    print(''.join(lines))

    result = []
    for i, line in enumerate(lines, start=1):
        words = re.findall(r"\b\w+(?:'\w+)?\b", line)  # используем регулярные выражения для разделения слов
        words = [word for word in words if word not in ["'s", "'t", "'ll", "'ve", "'re"]]  # исключаем указанные конструкции
        if words:  # проверка на наличие слов в строке
            most_common = Counter(words).most_common(1)
            if most_common:  # проверка на наличие повторяющихся слов
                most_common_word, count = most_common[0]
                if count >= 1:  # слово встречается не менее двух раз
                    result.append((i, most_common_word, count + 1))  # прибавляем 1 к числу повторений

    with open('output.txt', 'w') as file:
        for line_number, word, count in result:
            file.write(f"{line_number}. {word} -- {count}\n")

    # Вывод содержимого файла output.txt после завершения работы
    with open('output.txt', 'r') as file:
        print(file.read())

# Запуск функции
most_common_word_in_line('input.txt')
