import re

def censor_file(file_name, stop_words_file):
    # Чтение запрещенных слов из файла
    with open(stop_words_file, 'r') as file:
        stop_words = file.read().split()

    # Чтение и цензура текста из файла
    with open(file_name, 'r') as file:
        text = file.read()
        for word in stop_words:
            text = re.sub(r'\b' + word + r'\b', '*' * len(word), text, flags=re.IGNORECASE)

    # Вывод цензурированного текста
    print(text)

# Запуск функции
censor_file('text.txt', 'stop_words.txt')
