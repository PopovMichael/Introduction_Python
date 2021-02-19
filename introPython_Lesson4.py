# Обработка исключений
# Пример не правильной обработки исключений
value = input("Введите целое число: ")
if value.isdigit():  # тут выполнится проверка, состоит ли строка ввода из цифр
    value = int(value)
    result = value / 2
    print(result)
else:
    print("Не вверный ввод!")
    result = 0  # "умалчивание проблемы" - так лучше не делать, чтобы ошибка не
    # тянулась в коде к следующему этапу.
    # result = ""  # "пустая строка" - а это еще хуже, так мы еще и меняем тип

# Пример верной обработки исключений
value = input("Введите целое число: ")
try:
    value = float(value)
    result = 2 / value
    print(result)
# except:  # общее искючение для всех ошибок - лучше не использовать
# except (ValueError, TypeError)  # если нужно привести к одному виду несколько
# ошибок со схожим результатом.
except ValueError:  # исключение для конкретной ошибки
    print("Не вверный ввод!")
    value = 0  # по умолчанию, логика разрешает нам считать, что введен 0
    result = 1
    print(result)  # для проверки
except ZeroDivisionError:
    print("Деление на 0 не допустимо!")
    value = 0
    result = 1
    print(result)  # для проверки
except FileExistsError:
    pass


# Методы строк
my_str = "qwerty qwerty qwerty"
symbol = "ty"

result_1 = my_str.find(symbol)  # поиск первого вхождения символа(ов) в строке.
# В случае неудачи - вернет значение -1.
print(result_1)  # отобразит номер символа в строке
result_2 = my_str.rfind(symbol)  # поиск последнего вхождения символа(ов)
# в строке. В случае неудачи - вернет значение -1.
print(result_2)

result_3 = my_str.index(symbol)  # поиск первого вхождения символа(ов)
# в строке. В случае неудачи - уронит программу с ошибкой ValueError.
print(result_3)
result_4 = my_str.rindex(symbol)  # поиск последнего вхождения символа(ов)
# в строке. В случае неудачи - уронит программу с ошибкой ValueError.
print(result_4)

result_5 = my_str.replace(symbol, "TY")  # замена символа на другой. При чем,
# замена произойдет для всех найденных символов "symbol" на новый.
print(result_5)
# filename = filename.replace("jpeg", "jpg)  # доп. пример
result_6 = my_str.replace(symbol, "TY", 1)  # замена символа на другой. При чем,
# замена произойдет только для первого встречного символа (1/2). Если прописать
# "2" - то для 2/2 и т.д.
print(result_6)

test_str = "qwerty is default String"
# result_7 = test_str.capitalize()  # приведет первую букву в строке к верхнему
# регистру, но все остальные опустит до нижнего. Не лучший способ.
result_7 = test_str[0].upper() + test_str[1:]  # первый вариант
print(result_7)
result_8 = test_str.replace(test_str[0], test_str[0].upper(), 1)  # второй вариант
print(result_8)


# Цикл for
# Первый способ:
my_str = "test string"
# print(len(my_str))  # кол-во символов = кол-во циклов
for symbol_1 in my_str:
    # print(symbol_1)  # пример 1
    # print(symbol_1, my_str)  # пример 2
    # print(symbol_1 * 3)  # пример 3
    # print(symbol_1 + symbol_1)  # пример 4
    if symbol_1 in "eyuioa":  # распечатать только гласные, а если not in
        # - то не гласные.
        print(symbol_1)

my_str = "test strIng"
for symbol_2 in my_str:
    if symbol_2.lower() in "eyuioa" and symbol_2.isupper():  # распечатать только
        # гласные, да еще и начинающиеся с большой буквы).
        print(symbol_2)

# Второй способ:
my_str = "test string"
for index_1 in range(len(my_str)):
    print(index_1, my_str[index_1])  # реализован доступ по индексу

my_str = "test string"
for index_2 in range(len(my_str)):
    if not index_2 % 2:  # запись четного числа
        print(index_2, my_str[index_2])

# Пример подстановки индексов
my_string_1 = "test strIng"
my_string_2 = my_string_1.upper()
for index_3 in range(len(my_string_1)):
    print(index_3, my_string_1[index_3], my_string_2[index_3])

# Третий способ:
my_string_3 = "test strIng"
my_string_4 = my_string_3.upper()
for index_4, symbol_4 in enumerate(my_string_3):
    # print(index_4, symbol_4)
    if not index_4 % 2:
        print(index_4, symbol_4)


# Кортежи (tuple) - неизменяемый тип
my_tuple = (1, 2, 3, "4, 5, 6", 3.14, True, None)
# print(type(my_tuple), my_tuple)
print(my_tuple[5])  # запрос объекта из кортежа

point = (2, 4, -7)  # условная точка координат в пространстве
x_0 = point[0]
print(x_0)
x_0 += 2  # попытка изменить кортеж
point = (x_0, point[1], point[2])
print(point)  # кортеж изменен (переписан) верно


# Списки (list) - изменяемый тип
my_list = [1, (2, 3), "4, 5, 6", 3.14, True, None]
print(type(my_list), my_list)
print(my_list[1:4])

point = [2, 4, -7]
x_0 = point[0]
print(x_0)
x_0 += 2
point[0] = x_0  # изменение списка
print(point)  # список изменен

# Как с помощью списка "быстро" изменить кортеж:
my_tuple = (1, (2, 3), "4, 5, 6", 3.14, True, None)
my_tuple = list(my_tuple)
my_tuple[-1] = -1
my_tuple = tuple(my_tuple)
print(my_tuple)

my_list = [1, (2, 3), "4, 5, 6", 3.14, True, None]
for value in my_list:
    # print(value)  # просто распечатать
    if type(value) not in (str, int, bool):
        print(value)

new_list = []
for number in range(1, 6):
    value = number ** 2
    new_list.append(value)
print(new_list)
