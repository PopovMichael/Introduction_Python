# 1
# www = "www.google.com"  # вариант 1
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")
#
# # www = "www.google.com"  # вариант 2
# # if "com" in www:
# #     www = "com in www"
# # else:
# #     www = "com not in www"
# # print(www)
#
# # www = "www.google.com"  # вариант 3
# # www = "com in www" if "com" in www else "com not in www"
# # print(www)
#
# # 2
# www = "www.command_and_conquer.com"
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")
#
# # 3
# www = "www.command_and_conquer.net"
# if "com" in www:
#     print("com in www")
# else:
#     print("com not in www")
#
# # 4
# www = "www.command_and_conquer.net"
# if ".com" in www:
#     print("com in www")
# else:
#     print("com not in www")
#
# # 5
# www = "www.conquer_and_command.net"
# if ".com" in www:
#     print("com in www")
# else:
#     print("com not in www")

# 6
# value = 123
# my_str = str(value) if value < 200 else str(value % 10)
# print(my_str)
#
# # 7
# value = 321
# my_str = str(value) if value < 200 else str(value % 10)
# print(my_str)
#
# # 8
# value = 123
# my_str = str(value) if value < 200 else str(value)[::-1]
# print(my_str)
#
# # 9
# value = 321
# my_str = str(value) if value < 200 else str(value)[::-1]
# print(my_str)

# 10
# value = "123456789"
# my_str = value if len(value) < 5 else value[2:5]
# print(my_str)
#
# # 11
# value = "123456789"
# my_str = value if len(value) >= 5 else value[2:5]
# print(my_str)
#
# # 12. Нужно понять
# value = "123456789"
# my_str = value if len(value) < 5 else value[2:5:2]
# print(my_str)
#
# # 13
# value = "123456789"
# my_str = value if len(value) >= 5 else value[2:5:2]
# print(my_str)
#
# # 14
# value = "123456789"
# my_str = value if len(value) <= 5 else value[2:5]
# print(my_str[::-1])
#
# # 15
# value = "123456789"
# my_str = value if len(value) >= 5 else value[2:5]
# print(my_str[::-1])
#
# # 16
# value = "123456789"
# my_str = value if len(value) <= 5 else value[2:5:2]
# print(my_str[::-1])

# 17. Нужно понять
# count = 10
# while count > 0:
#     print("Test")  # бесконечный цикл

# 18. Нужно понять
# count = 10
# while count > 0:
#     print("Test")
#     count -= 1  # "-=" - знак вычитания, совмещённого с присваиванием

# 19. Нужно понять
count = 10
exit_flag = True
while exit_flag:
    count -= 0
    if count > 0:
        exit_flag = False
    print("Test")
