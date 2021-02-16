# Условный оператор if (синтаксис)
# if условие:
#   блок действий если условие "Да (+)"
# elif условие 2:
#   блок действий если условие 2 "Да (+)"
# elif n...
# else:
#   блок действий если условие "Нет (-)"
if 4 < 20:
    print("Верно")  # если условие "Да", то увидим результат, если нет - будет пусто

value = int(input("Введите целое число >= 10: "))
if value >= 10:
    print("Верно")
else:
    print("Не верно")

value = int(input("Какая температура на улице? "))
if value < 0:
    print("Не забудь надеть шапку!")
elif value > 0:
    print("Можешь не надевать шапку.")
else:
    print("Возьми с собой шапку.")

# Тернарный оператор
value = int(input("Какая температура на улице? "))
# result = "Холодно"  # 2-й вариант, не самый удачный
if value >= 0:
    result = "Не холодно"
else:
    result = "Холодно"  # 1-й вариант, лучший
print(result)

value = int(input("Какая температура на улице? "))
result = "Не холодно" if value >= 0 else "Холодно"
print(result)  # пример тернарного оператора в действии

# Цикл while
value = input("Введите свое имя: ")
if value:
    print("Спасибо! Вы прошли проверку,", value)
else:
    print("Имя не введено!")  # тут цикла еще нет

value = input("Введите свое имя: ")
while not value:  # без "not" будет работать не в том направлении
    value = input("Введите свое имя: ")
print("Спасибо! Вы прошли проверку,", value)

# Примеры бесконечного цикла: грубая ошибка
# while True:  # если прописать там False, ничего не будет
#     print("Бесконечность...")
# value = input("Введите свое имя: ")
# while value:
#     print(value)

# Пример цикла, который нарушен сменой имени переменной
# value = input("Введите свое имя: ")
# while not value:  # без "not" будет работать не в том направлении
#     new_value = input("Введите свое имя: ")  # нельзя менять переменную
# print("Спасибо! Вы прошли проверку,", value)

# Программа: игра - угадай цифру, что загадал компьютер
# Работа цикла через условие
from random import randint  # запрос из библиотеки, которая дает случайные числа
goal = randint(1, 100)  # цель = случайное число с диапазона: 1, 100
# print(goal)  # если просто нужно выводить случайные числа через print
value = int(input("Какое число я загадал? "))
while value != goal:
    if value > goal:
        value = int(input("Не угадал, пробуй меньше: "))
    else:
        value = int(input("Не угадал, пробуй больше: "))
print("Угадал!")  # цикл через условие

# Работа цикла через "разрыв"
from random import randint
goal = randint(1, 100)
value = int(input("Какое число я загадал? "))
while True:
    if value > goal:
        value = int(input("Не угадал, пробуй меньше: "))
    elif value < goal:
        value = int(input("Не угадал, пробуй больше: "))
    else:
        break  # точка выхода из текущего цикла
print("Угадал!")  # цикл через break-разрыв - не самый лучший подход

# Работа цикла через состояние
from random import randint
goal = randint(1, 100)
value = int(input("Какое число я загадал? "))
done = False  # это переменная состояния
while not done:
    if value > goal:
        value = int(input("Не угадал, пробуй меньше: "))
    elif value < goal:
        value = int(input("Не угадал, пробуй больше: "))
    else:
        done = True  # изменение состояния - точка выхода из цикла
print("Угадал!")  # цикл через состояние - гибкий подход к результату

# Форматирование строк
my_str = "qwerty"
print("my_str =", my_str)  # пример приведения переменных

path = "/home/mp/lessons"
filename = "python_lesson3.py"
full_path = path + "/" + filename
print(full_path)  # грубый вариант, но рабочий вариант форматирования строк

path = "/home/mp/lessons"
filename = "python_lesson3.py"
full_path = f"{path}/{filename}"
print(full_path)  # лучший вариант форматирования строк

path = "/home/mp/lessons"
filename = "python_lesson3.py"
full_path = "{}/{}".format(path, filename)
print(full_path)  # устаревший вариант форматирования строк

# Что можно делать со строкой
path = "/home/mp/lessons"
filename = "python_lesson3.py"
full_path = f"{path}/{filename}"
print(full_path)
print(full_path[0])  # обратиться к конкретному символу. 0 соответствует символу 1
print(full_path[-1])  # обратиться к символу c конца. -1 соответствует символу 1
print(len(full_path))  # узнать длину всей строки (кол-во символов),
# с возможностью указать конкретный символ или диапазон.
print(full_path[2:-2])  # срез в строке. С 3-го символа в начале,
# до предпоследнего символа в конце.
print(full_path[2:6])  # срез с конкретного символа по конкретный
print(full_path[:6])  # срез с начала строки по 6-й символ
print(full_path[6:])  # срез с 6-го символа до конца строки
print(full_path[::2])  # срез в строке с шагом через 1 c первого символа
print(full_path[1::2])  # срез в строке с шагом через 1 со втрого символа
print(full_path[::-1])  # разворот строки

# Оператор in. Позволяет выполнить запрос конкретного символа/массива в виде
# строки из строки, с помощью проверки условия через if, while.
www = "www.google.com"
result = str(input("Ваш поисковой запрос: "))
while result not in www:
    print("No!")
    result = str(input("Ваш поисковой запрос: "))
else:
    print("Yes!")
