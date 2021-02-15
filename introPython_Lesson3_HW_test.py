# 1
www = "www.google.com"  # вариант 1
if "com" in www:
    print("com in www")
else:
    print("com not in www")

# www = "www.google.com"  # вариант 2
# if "com" in www:
#     www = "com in www"
# else:
#     www = "com not in www"
# print(www)

# www = "www.google.com"  # вариант 3
# www = "com in www" if "com" in www else "com not in www"
# print(www)

# 2
www = "www.command_and_conquer.com"
if "com" in www:
    print("com in www")
else:
    print("com not in www")

# 3
www = "www.command_and_conquer.net"
if "com" in www:
    print("com in www")
else:
    print("com not in www")

# 4
www = "www.command_and_conquer.net"
if ".com" in www:
    print("com in www")
else:
    print("com not in www")

# 5
www = "www.conquer_and_command.net"
if ".com" in www:
    print("com in www")
else:
    print("com not in www")

# 6
value = 123
my_str = str(value) if value < 200 else str(value % 10)
print(my_str)

# 7
value = 321
my_str = str(value) if value < 200 else str(value % 10)
print(my_str)

# 8
value = 123
my_str = str(value) if value < 200 else str(value)[::-1]
print(my_str)

# 9
value = 321
my_str = str(value) if value < 200 else str(value)[::-1]
print(my_str)

# 10
value = "123456789"
my_str = value if len(value) < 5 else value[2:5]
print(my_str)

# 11
value = "123456789"
my_str = value if len(value) >= 5 else value[2:5]
print(my_str)

# 12
value = "123456789"
my_str = value if len(value) < 5 else value[2:5:2]  # шаг на 2 в диапазоне от 1
print(my_str)

# 13
value = "123456789"
my_str = value if len(value) >= 5 else value[2:5:2]
print(my_str)

# 14
value = "123456789"
my_str = value if len(value) <= 5 else value[2:5]
print(my_str[::-1])

# 15
value = "123456789"
my_str = value if len(value) >= 5 else value[2:5]
print(my_str[::-1])

# 16
value = "123456789"
my_str = value if len(value) <= 5 else value[2:5:2]
print(my_str[::-1])

# 17
# count = 10
# while count > 0:
#     print("Test")  # бесконечный цикл, так как нет точки выхода из цикла

# 18
count = 10
while count > 0:
    print("Test")
    count -= 1  # "-=" - знак вычитания, совмещённого с присваиванием
# Как работает: после каждого цикла из исходного значения count(10) вычитается 1
# с последующим присваиванием нового значения count(10-1=9), до тех пор,
# пока условие не будет выполнено до 0 - count(1-1=0) - точка выхода.
# Для проверки можно просто поделить 10 на 1 и узнать сколько будет повторений
# в цикле до выхода из него.

# 19
count = 10
exit_flag = True
while exit_flag:
    count -= 0
    if count > 0:
        exit_flag = False  # точка выхода
    print("Test")
# Как работает: если бы у нас не было "if", то цикл был бы бесконечным, так как
# внутри цикла условие True замкнуто и не имеет условия для выхода (10-0=10).
# В данном случае, после первого оборота, цикл пишет Test (так как True), а
# затем выполняет проверку значения (count > 0), при котором выполняется
# наша точка выхода - False. И Test больше не выводит.
