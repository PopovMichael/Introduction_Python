# 1
# Дано целое число (int). Определить сколько нулей в этом числе.
number = 123045607890
my_number = 0
count = str(number).count(str(my_number))
print(count)

###############

# 2
# Дано целое число (int). Определить сколько нулей в конце этого числа.
number = 100100010000
count = 0
while not number % 2:
    count += 1
    number //= 2
print(count)

###############

# 3a
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить элементы на
# четных местах из my_list_1, а потом все элементы на нечетных
# местах из my_list_2.
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

#####

# 3b
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить четные элементы
# (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1, 3, 2, 4, 5], my_list_2 = [10, 20, 15, 25, 22]
# my_result [2, 4, 15, 25]
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for value in my_list_1:
    if value % 2:
        my_list_1.remove(value)
for value in my_list_2:
    if not value % 2:
        my_list_2.remove(value)
my_result = my_list_1 + my_list_2
print(my_result)

###############

# 4
# Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый
# элемент из my_list стоит на последнем месте.
# Если my_list [1, 2, 3, 4], то new_list [2, 3, 4, 1].
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()[1::]
new_list.append(my_list[0])
print(new_list)

###############

# 5
# Дан список my_list. В ЭТОМ списке первый элемент переставить на
# последнее место. [1, 2, 3, 4] > [2, 3, 4, 1]. Пересоздавать список
# нельзя! (используйте метод pop).
my_list = [1, 2, 3, 4, 5]
my_list.append(my_list.pop(0))
print(my_list)

###############

# 6
# Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ
# (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
my_str = "43 больше чем 34 но меньше чем 56"
my_list = sorted(my_str.split(" "))
result = int(my_list[0]) + int(my_list[1]) + int(my_list[2])
print(result)  # решение примера

my_new_str = "12 08 1993"
my_new_list = my_new_str.split(" ")
new_result = int(my_new_list[0]) + int(my_new_list[1]) + int(my_new_list[2])
print(new_result)  # мой пример

###############

# 7
# Дана строка my_str. Разделите эту строку на пары из двух символов и
# поместите эти пары в список. Если строка содержит нечетное количество
# символов, пропущенный второй символ последней пары должен быть заменен
# подчеркиванием ('_').
# Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
my_str = "11223344556"
if not len(my_str) % 2:
    my_list = [my_str[x:x + 2] for x in range(0, len(my_str), 2)]
else:
    my_list = [my_str[x:x + 2] for x in range(0, len(my_str) - 1, 2)]
    my_list.append(my_str[-1] + "_")
print(my_list)

###############

# 8
# Дана строка my_str в которой символы не повторяются и два символа
# l_limit и r_limit, которые точно находятся в этой строке.
# Причем l_limit левее чем r_limit. В переменную sub_str поместить часть
# строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
sub_str = my_str[my_str.index(l_limit) + 1: my_str.index(r_limit)]
print(sub_str)

###############

# 9
# Дана строка my_str в которой символы МОГУТ повторяться и два символа
# l_limit, r_limit, которые точно находятся в этой строке.
# Причем l_limit левее чем r_limit. В переменную sub_str поместить
# НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o",
# r_limit = "g" -> sub_str = "ng strin".
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]
print(sub_str)

###############

# 10
# Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ
# КОЛИЧЕСТВО таких элементов. Крайние элементы списка никогда не учитываются,
# поскольку у них недостаточно соседей. Для списка [2, 4, 1, 5, 3, 9, 0, 7]
# ответом будет 3 потому что 4 > 2 + 1, 5 > 1 + 3, 9 > 3 + 0.
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
count = 0
for i in range(len(my_list[1:])):
    sum = my_list[i - 1] + my_list[i + 1]
    if my_list[i] > sum:
        count += 1
print(count)
