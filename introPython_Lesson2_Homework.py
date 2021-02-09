a = 'Hello, "A"'
b = a  # "b" приняло значение "a"
c = 'Hello, "B"'
b = c  # "b" приняло значение "c", значение "a" вернулось к исходному
c = a  # "c" приняло значение "a", значение "b" вернулось к исходному
a = b  # "a" приняло значение "b"
print(a)

my_value_1 = 2
my_value_2 = "4"
print(my_value_1 * my_value_2)

my_value_1 = 2
my_value_2 = "4"
my_value_1 = str(my_value_1)
my_value_2 = int(my_value_2)
print(my_value_1 * my_value_2)

my_value_1 = 2
my_value_2 = "4"
my_value_2 = int(my_value_2)
print(my_value_1 * my_value_2)

my_value_1 = 2
my_value_2 = "4"
my_value_1 = str(my_value_1)
print(my_value_1 + my_value_2)

my_value = 12
my_bool = my_value % 3 == 0
print(my_bool)

my_value = 12
my_bool_1 = my_value % 3 == 0
my_bool_2 = my_value % 2 == 0
print(my_bool_1 and my_bool_2)

my_value = 14
my_bool_1 = my_value % 3 == 0
my_bool_2 = my_value % 2 == 0
print(my_bool_1 or my_bool_2)

my_value = 7
my_bool_1 = my_value % 3 == 0
my_bool_2 = my_value % 2 == 0
print(not my_bool_1 or not my_bool_2)

value = input("Введите число: ")
value = int(value)
if value % 2 == 0 and value % 3 == 0:
    print("Число делится на 6")
elif value % 2 == 0:
    print("Число делится на 2")
elif value % 3 == 0:
    print("Число делится на 3")
else:
    print("Число не делится ни на 2, ни на 3")

###############################

numb_1 = input("Введите целое число, чтобы умножить его на 2: ")
value = int(numb_1)
print(value * 2)

numb_2 = input("Введите целое число, чтобы умножить его на 2: ")
value = float(numb_2)
print(value * 2)

numb_3 = input("Введите значение, чтобы задвоить его: ")
value = str(numb_3)
print(value * 2)
