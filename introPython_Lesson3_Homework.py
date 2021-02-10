# 1. У вас есть переменная value, тип - int.
# Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value,
# в противном случае - противоположное value число.
value = int(input("1.1. Введите целое число: "))  # вариант 1
if value < 100:
    new_value = value / 2
else:
    new_value = value * -1
print(new_value)

value = int(input("1.2. Введите целое число: "))  # вариант 2
new_value = value / 2 if value < 100 else value * -1
print(new_value)

#####################################################

# 2. У вас есть переменная value, тип - int.
# Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0.
value = int(input("2.1. Введите целое число: "))  # вариант 1
if value < 100:
    new_value = 1
else:
    new_value = 0
print(new_value)

value = int(input("2.2. Введите целое число: "))  # вариант 2
new_value = value != 0 if value < 100 else value == 0
print(int(new_value))  # если не поставить int, то будет True/False, вместо 1/0

#####################################################

# 3. У вас есть переменная value, тип - int.
# Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False.
value = int(input("3.1. Введите целое число: "))  # вариант 1
if value < 100:
    new_value = True
else:
    new_value = False
print(new_value)

value = int(input("3.2. Введите целое число: "))  # вариант 2
new_value = value != 0 if value < 100 else value == 0
print(new_value)

#####################################################

# 4. У вас есть переменная my_str, тип - str.
# Заменить в my_str все маленькие буквы на большие.
my_str = str(input("4. Введите любое слово: "))
print(my_str.upper())

#####################################################

# 5. У вас есть переменная my_str, тип - str.
# Заменить в my_str все большие буквы на маленькие.
my_str = str(input("5. Введите любое слово: "))
print(my_str.lower())

#####################################################

# 6. У вас есть переменная my_str, тип - str.
# Если ее длина меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer".
# Если длина не меньше 5, то оставить строку как есть.
my_str = str(input("6.1. Введите любое слово: "))  # вариант 1
if len(my_str) < 5:
    my_str = my_str * 2
else:
    my_str = my_str
print(my_str)

my_str = str(input("6.2. Введите любое слово: "))  # вариант 2
my_str = my_str * 2 if len(my_str) < 5 else my_str
print(my_str)

# 7. У вас есть переменная my_str, тип - str.
# Если ее длина меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq".
# Если длина не меньше 5, то оставить строку как есть.
my_str = str(input("7.1. Введите любое слово: "))  # вариант 1
if len(my_str) < 5:
    my_str = my_str + my_str[::-1]
else:
    my_str = my_str
print(my_str)

my_str = str(input("7.2. Введите любое слово: "))  # вариант 2
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)
