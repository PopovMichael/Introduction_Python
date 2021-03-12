# 1
# Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку: "qwe" на "ewq". Если на четном - оставить
# без изменения. Задание сделать с использованием enumerate.
my_list = ["sword", "shield", "bow", "arrows"]
new_list = []
for index, string in enumerate(my_list):
    if not index % 2:
        new_list.append(string)
    else:
        new_list.append(string[::-1])
print(new_list)

####################

# 2
# Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ["sword", "shield", "bow", "arrows", "adventure"]
new_list = []
for string in my_list:
    if string.startswith("a"):
        new_list.append(string)
print(new_list)

####################

# 3
# Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list, в которых есть символ - буква "a" на любом месте.
my_list = ["human", "elf", "dwarf", "the one ring"]
new_list = []
for string in my_list:
    if "a" in string:
        new_list.append(string)
print(new_list)

####################

# 4
# Дан список my_list в котором могут быть как строки (type str),
# так и целые числа (type int). Создать новый список в который
# поместить только строки из my_list.
my_list = ["human", 5000, "elf", 500, "dwarf", 1000, "army"]
new_list = []
for string in my_list:
    string = str(string)
    if string.isalpha():
        new_list.append(string)
print(new_list)

####################

# 5
# Дана строка my_str. Создать список в который поместить те символы
# из my_str, которые встречаются в строке только один раз.
my_str = "The army of humans, elves and dwarves"
my_list = []
for symbol in my_str:
    count = my_str.count(symbol)
    if count == 1:
        my_list.append(symbol)
print(my_list)

####################

# 6
# Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
my_str_1 = "Humans of Gondor, elves from Rivendell"
my_str_2 = "Orcs of Mordor, goblins from Moria"
my_list = []
for symbol in my_str_1:
    if symbol in my_str_1 and symbol in my_str_2:
        my_list.append(symbol)
print(my_list)

####################

# 7
# Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках, но в каждой только по одному разу.
my_str_1 = "Humans of Gondor, elves from Rivendell"
my_str_2 = "Orcs of Mordor, goblins from Moria"
my_list = []
for symbol in my_str_1:
    count_1 = my_str_1.count(symbol)
    count_2 = my_str_2.count(symbol)
    if symbol in my_str_1 and symbol in my_str_2:
        if count_1 == 1 and count_2 == 1:
            my_list.append(symbol)
print(my_list)

####################

# 8
# Описать с помощью словаря следующую структуру для конкретного
# человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
print("Данные персонажа:")
title_name_age = {"Титул": "Король",
                  "Имя": "Арагорн II Элессар",
                  "Возраст": 210}
family = {"Супруга": "Арвен",
          "Наследник": "Эльдарион"}
throne = {"Материк": "Средиземье",
          "Страна": "Воссоединённое королевство Арнора и Гондора",
          "Столица": "Минас Тирит"}
resume = {"Титул, имя и возраст": title_name_age,
          "Семья": family,
          "Престол": throne}
print(resume)

####################

# 9
# Описать с помощью словаря следующую структуру
# (рецепт ненастоящего торта, придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
print("Рецепт торта «Кучерявый Пинчер» на 12 порций")
cakes = {"Яйца:": "3 шт",
         "Сметана:": "200 грамм",
         "Сгущенное молоко:": "190 грамм",
         "Какао:": "20 грамм",
         "Мука:": "250 грамм",
         "Ванилин:": "1 пакетик",
         "Разрыхлитель:": "1 ст.л"}
cream = {"Сметана:": "1000 грамм",
         "Саханая пудра:": "1 стакан"}
glaze = {"Какао:": "20 грамм",
         "Сахар": "70 грамм",
         "Молоко:": "50 мл",
         "Сливочное масло:": "50 мл",
         "Вешневый джем": "100 грамм"}
recipe = {"Коржи": cakes,
          "Крем": cream,
          "Глазурь": glaze}
print(recipe)
