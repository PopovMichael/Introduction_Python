import random as rd

# 1
# Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
my_random_list = []
while not len(my_random_list) == 20:
    my_random_list.append(rd.randint(1, 100))
print(my_random_list)

####################
print("----------")

# 2
# Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с
# помощью модуля random в диапазоне от -10 до 10 по каждой оси.
triangle = {"A": (rd.randint(-10, 10),
                  rd.randint(-10, 10),
                  rd.randint(-10, 10)),
            "B": (rd.randint(-10, 10),
                  rd.randint(-10, 10),
                  rd.randint(-10, 10)),
            "C": (rd.randint(-10, 10),
                  rd.randint(-10, 10),
                  rd.randint(-10, 10))
            }
print(triangle)

####################
print("----------")

# 3
# Создать функцию my_print, которая принимает в виде параметра строку
# и печатает ее с тремя символами * вначале и в конце строки.
# Пример:
# my_str = "I'm the string"
# Печатает ***I'm the string***
my_str = "I'm the string"


def my_print(my_str):
    print("***" + my_str + "***")


my_print(my_str)

####################
print("----------")

# 4
# Дан список словарей persons в формате [{"name": "John", "age": 15},
# ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает
# - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает
# - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
dwarves = [{"name": "Торин", "age": 175},
           {"name": "Балин", "age": 281},
           {"name": "Двалин", "age": 219},
           {"name": "Фили", "age": 89},
           {"name": "Кили", "age": 89},
           {"name": "Оин", "age": 240},
           {"name": "Глоин", "age": 202},
           {"name": "Ори", "age": 75},
           {"name": "Нори", "age": 136},
           {"name": "Дори", "age": 174},
           {"name": "Бифур", "age": 144},
           {"name": "Бофур", "age": 169},
           {"name": "Бомбур", "age": 198}, ]
ages = []
names = []
the_youngest = []
longest_name = []
for person in dwarves:
    ages.append(person["age"])
    names.append(len(person["name"]))
for person in dwarves:
    if min(ages) == person["age"]:
        the_youngest.append(person["name"])
    if max(names) == len(person["name"]):
        longest_name.append(person["name"])
average_age = sum(ages) // len(ages)
print(f"а) Самый молодой гном: {the_youngest}")
print(f"б) Обладатель самого длинного имени: {longest_name}")
print(f"в) Средний возраст всех гномов: {average_age}")

####################
print("----------")

# 5
# Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
#   если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#   если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}
my_dict_1 = {"name": "Торин", "age": 175, "title": "Король гномов", "sword": "Оркрист"}
my_dict_2 = {"name": "Гэндальф", "title": "Серый маг", "sword": "Гламдринг", "ring": "Нарья"}
keys = []
my_dict_4 = {}

keys_1 = set(my_dict_1.keys())
keys_2 = set(my_dict_2.keys())

for key in keys_1.union(keys_2):
    if key in keys_1 and key in keys_2:
        keys.append(key)
print("а)", keys)

keys_1.difference_update(keys_2)
dif_keys = list(keys_1)
print("б)", dif_keys)

my_dict_3 = dict((key, my_dict_1[key]) for key in my_dict_1 if key not in my_dict_2)
print("в)", my_dict_3)

for key in keys_1.union(keys_2):
    if key in my_dict_1 and key in my_dict_2:
        my_dict_4[key] = [my_dict_1[key], my_dict_2[key]]
    elif key in my_dict_1 and key not in my_dict_2:
        my_dict_4[key] = my_dict_1[key]
    else:
        my_dict_4[key] = my_dict_2[key]
print("г)", my_dict_4)
