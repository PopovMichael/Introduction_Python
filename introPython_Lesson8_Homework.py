import random
import json

# 1
# Считать данные из файла names.txt и поместить в список только фамилии из
# файла. Каждая строка файла содержит номер, фамилию, страну, некоторое
# число (таблица взята с википедии). Фамилия находится всегда на одной и
# той же позиции в строке.
with open("names.txt", "r") as name_file:
    names = []
    for line in name_file.readlines():
        line = line.replace(".", "")
        names.append(line.split('\t')[1])
print(names)


####################

# 2
# Создать функцию для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее
# 5 но не более 20 ключей). Ключи - уникальные случайные строки длинны 5
# символов из маленьких букв английского алфавита (можно с повторениями
# символов). Значения - или целое число в диапазоне от -100 до 100, или
# число типа float в диапазоне от 0 до 1, или True/False. Выбор значения
# должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
def create_random_key():
    key = "".join(chr(random.randint(ord("a"), ord("z"))) for _ in range(5))
    return key


def create_value():
    n = random.randrange(3)
    if n == 0:
        value = random.randint(-100, 100)
    elif n == 1:
        value = random.uniform(0, 1)
    else:
        value = bool(random.randint(0, 1))
    return value


def create_dict():
    my_dict = {}
    n = random.randint(5, 20)

    for item in range(n):
        key = create_random_key()
        value = create_value()
        my_dict[key] = value
    return my_dict


####################

# 3
# Написать функцию generate_and_write_json которая принимает один параметр
# - полный путь к файлу. Cгенерировать данные для записи с помощью функции
# из пункта 2 и записать в данный файл.

def write_json(filename):
    with open(filename, "w") as json_file:
        json.dump(create_dict(), json_file, indent=2)


def generate_and_write_file(filename):
    my_format = filename.split('.')[-1]
    result = write_json(filename)
    return result


generate_and_write_file("test.json")
