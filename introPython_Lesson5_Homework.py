# 1
# Дано целое число (int). Определить сколько нулей в этом числе.
number = 123045607890
zero = 0
count = str(number).count(str(zero))
print(count)

# 2
# Дано целое число (int). Определить сколько нулей в конце этого числа.
number = 100100010000
count = 0
while not number % 2:
    count += 1
    number //= 2
print(count)
