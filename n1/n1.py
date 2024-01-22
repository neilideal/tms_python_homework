import os
import random
import string
import shutil

def print_directory_contents():
    print("Содержимое текущей директории:")
    print(os.listdir())
    print()

# Вывести имя вашей ОС
print(f"Операционная система: {os.name}")

# Вывести путь до папки, в которой вы находитесь
print(f"Текущая директория: {os.getcwd()}")

# Создать 30 тысяч файлов всех известных системе расширений со случайным названием
extensions = ['.txt', '.jpg', '.png', '.pdf', '.docx']  # добавьте больше расширений по мере необходимости
for i in range(30000):
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    random_extension = random.choice(extensions)
    with open(f"{random_name}{random_extension}", 'w') as f:
        pass

print_directory_contents()

# Рассортировать файлы по расширениям
for extension in extensions:
    os.makedirs(extension, exist_ok=True)
    for file in os.listdir():
        if file.endswith(extension):
            shutil.move(file, extension)

print_directory_contents()

# После рассортировки выводится сообщение
for extension in extensions:
    folder_size = sum(os.path.getsize(f"{extension}/{f}") for f in os.listdir(extension) if os.path.isfile(f"{extension}/{f}"))
    print(f"В папке с {extension} файлами перемещено {len(os.listdir(extension))} файлов, их суммарный размер - {folder_size / (1024 ** 3)} гигабайт")

# Как минимум один файл в любой из получившихся поддиректорий переименовать
for extension in extensions:
    files = os.listdir(extension)
    if files:
        old_file = files[0]
        new_file = "new_" + old_file
        os.rename(f"{extension}/{old_file}", f"{extension}/{new_file}")
        print(f"Файл {old_file} был переименован в {new_file}")
        break

print_directory_contents()