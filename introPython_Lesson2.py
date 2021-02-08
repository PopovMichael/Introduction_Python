# Типы данных:
#   int - целое число
#   float - число с точкой
#   str - строка
# функция type() покажет какого типа заданное значение

a = 10  # int
print(a, type(a))
a = 1.0  # float
print(a, type(a))
a = "10"  # str
print(a, type(a))

# Пример
a = 12
b = 8
c = a + b  # 20
a = c * b  # 20 * 8 = 160 / значение "a" переписано
b = a - b - c  # 160 - 8 - 20 = 132 / значение "b" переписано
print(b)

my_full_number = 10
print(my_full_number, type(my_full_number))
my_float_number = 1.0
print(my_float_number, type(my_full_number))
my_str = "10"
print(my_str, type(my_str))

my_str = input("Поздоровайся со мной: ")
my_str = str(my_str)
print(my_str, type(my_str))

my_full_number = input("Введите целое число: ")
my_full_number = int(my_full_number)
print(my_full_number, type(my_full_number))

my_float_number = input("Введите целое число еще раз: ")
my_float_number = float(my_float_number)
print(my_float_number, type(my_float_number))

numb_1 = input("Введите значение: ")
numb_1 = str(numb_1)  # можно задать нужный тип
numb_2 = input("Введите целое число: ")
numb_2 = int(numb_2)  # можно задать нужный тип
result = numb_1 * numb_2
print(result)

test_str = "-100.95"  # меняем значение строки с дальнейшим преображением
value = float(test_str)
print(value, type(value))
value = int(value)
print(value, type(value))
value = str(value)
print(value, type(value))

# bool (not bool), True, False
# == равно, >= <= больше/меньше или равно, != не равно
my_bool = 22 != 22
print(my_bool)
value = number = 5
print(str(my_bool))

test_value = "False"
print(bool(test_value))

value = bool("1") or bool("2")
print(value)
value = bool("qwe") and (bool("q") or bool(""))
print(value)
