# Перенести код ДЗ №8 в класс (см. урок 13)
import random
import string


def create_random_str(min_limit, max_limit):
    limit_value = random.randint(min_limit, max_limit)
    symbols = string.ascii_lowercase + string.digits
    random_str = "".join(random.sample(symbols, limit_value))
    # return random_str
    print(random_str)  # для проверки


create_random_str(2, 18)

####################

# def create_random_number():
#     random_number = random.randint(100, 999)
#     return random_number
#
#
# def create_random_str():
#     random_string = [chr(number) for number in range(ord('a'), ord('z') + 1)]
#     random_string = "".join([random.choice(random_string) for element in range(random.randint(5, 7))])
#     return random_string
#
#
# names = ["Martin", "John", "Victoria", "Olaf", "Gustav", "Enrique"]
# domains = ["uk", "us", "it", "no", "de", "es"]
#
#
# def create_email(names, domains):
#     random_name = random.choice(names)
#     random_domain = random.choice(domains)
#     random_number = create_random_number()
#     random_string = create_random_str()
#     result = f"{random_name.lower()}.{random_number}@{random_string}.{random_domain}"
#     return result
#
#
# e_mail = create_email(names, domains)
# print(e_mail)
