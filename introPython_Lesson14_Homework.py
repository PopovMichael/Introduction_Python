# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов,
# максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).
#
# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 10
        self.strength = 1
        self.agility = 1
        self.intelligence = 1
        self.additional_characteristic = ""

    def __repr__(self):
        return f"Имя: {self.name}; " \
               f"Клан: {self.clan}; " \
               f"Усиленный навык: {self.additional_characteristic}; " \
               f"Здоровье: {self.health}, " \
               f"Сила: {self.strength}, " \
               f"Ловкость: {self.agility}, " \
               f"Интеллект: {self.intelligence}"

    def healing(self):
        self.health += 10
        if self.health >= 100:
            self.health = 100

    def increase_skill(self):
        if self.clan == "Коллегия Винтерхолда (Маги)":
            self.intelligence += 1
            if self.intelligence >= 10:
                self.intelligence = 10
        if self.clan == "Гильдия Воров (Лучники)":
            self.agility += 1
            if self.agility >= 10:
                self.agility = 10
        if self.clan == "Соратники (Рыцари)":
            self.strength += 1
            if self.strength >= 10:
                self.strength = 10


class Mage(Unit):

    def __init__(self, name, clan, magic_type):
        super().__init__(name, clan)
        self.additional_characteristic = magic_type


class Archer(Unit):

    def __init__(self, name, clan, bow_type):
        super().__init__(name, clan)
        self.additional_characteristic = bow_type


class Knight(Unit):

    def __init__(self, name, clan, weapon_type):
        super().__init__(name, clan)
        self.additional_characteristic = weapon_type


mage = Mage("Архимаг Урусон", "Коллегия Винтерхолда (Маги)", "Огонь")
print(mage)  # до улучшения характеристик
mage.increase_skill()
mage.healing()
print(mage)
archer = Archer("Астрид", "Гильдия Воров (Лучники)", "Арбалет")
print(archer)  # до улучшения характеристик
archer.increase_skill()
archer.healing()
print(archer)
knight = Knight("Галмар", "Соратники (Рыцари)", "Топор")
print(knight)  # до улучшения характеристик
knight.increase_skill()
knight.healing()
print(knight)
