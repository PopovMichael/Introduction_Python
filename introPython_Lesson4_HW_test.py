# 1
values = [1, 2, 3, 4, 5]
print(type(values))  # <class 'list'>

# 2
values = (1, 2, 3, 4, 5)
print(type(values))  # <class 'tuple'>

# 3
values = (1, 2, 3, 4, 5)
values = list(values)
print(type(values))  # <class 'list'>

# 4
values = [1, 2, 3, 4, 5]
values = tuple(values)
print(type(values))  # <class 'tuple'>

# 5 - нужно понять
values = [1, 2, 3, 4, 5]
result = []
for value in values:
    result.append(value)
print(result)  # [1, 2, 3, 4, 5]

# 6 - нужно понять
values = [1, 2, 3, 4, 5]
result = []
for value in values[::-1]:
    result.append(value)
print(result)  # [5, 4, 3, 2, 1]

# 7
values = [1, 2, 3, 4, 5]
print(len(values))  # 5

# 8
values = [1, 2, 3, 4, 5]
new_value = values + values[::-1]
print(new_value)  # [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

# 9
values = [1, 2, 3, 4, 5]
new_value = values
new_value.append(6)
print(values)  # [1, 2, 3, 4, 5, 6]

# 10 - нужно понять
values = [1, 2, 3, 4, 5]
new_value = values.copy()
new_value.append(6)
print(values)  # [1, 2, 3, 4, 5]

# 11 - нужно понять
values = [0] * 6
values[0] = 1
print(values)  # [1, 0, 0, 0, 0, 0]

# 12
value = 0
values = [value] * 6
value = 1
print(values)  # [0, 0, 0, 0, 0, 0]

# 13 - нужно понять
my_list = [0]
values = [my_list] * 3
print(values)  # [[0], [0], [0]]

# 14 - нужно понять
my_list = [0]
values = [my_list] * 3
my_list.append(1)
print(values)  # [[0, 1], [0, 1], [0, 1]]

# 15
my_list = [0]
values = [my_list.copy()] * 3
my_list.append(1)
print(values)  # [[0], [0], [0]]

# 16
my_list = ["a", "b", "c", "d", "e", "f"]
my_str = " ".join(my_list)  # разрыв между символами зависит от символа в ""
print(my_str)  # a b c d e f

# 17
my_list = ["a", "b", "c", "d", "e", "f"]
my_str = "_".join(my_list)
print(my_str)  # a_b_c_d_e_f

# 18
my_list = ["a", "b", "c", "d", "e", "f"]
my_str = "_".join(my_list[::-1])
print(my_str)  # f_e_d_c_b_a

# 19
my_list = ["a", "b", "c", "d", "e", "f"]
my_str = "".join(my_list[::2])
print(my_str)  # ace
