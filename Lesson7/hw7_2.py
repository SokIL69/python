# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
#       для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
#
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
#       реализовать абстрактные классы для основных классов проекта,
#       проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

caption = f'Основы языка Python. Урок 7. Домашнее задание 2.\n'
print(caption)

class Clothe(ABC): # Базовый класс
    _fabric_consumption = 0 # Общий расход ткани
    _coat = 0 # Количество пальто
    _suit = 0 # Количество костюмов

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothe): # пальто

    def __init__(self, name, size):
        super().__init__(name)
        if size > 55:
            size = 55
        self.size = size # размер
        Clothe._fabric_consumption += round(self.size/6.5 + 0.5, 2)
        Clothe._coat += 1

    @property
    def consumption(self):
        """ Определяет расхода ткани """
        return round(self.size/6.5 + 0.5, 2)

class Suit(Clothe): # костюм

    def __init__(self, name, growth):
        super().__init__(name)
        if growth > 2.2:
            growth = 2.2
        self.growth = growth # рост
        Clothe._fabric_consumption += round(2*self.growth + 0.3, 2)
        Clothe._suit += 1

    @property
    def consumption(self):
        """ Определяет расхода ткани """
        return 2*self.growth + 0.3


coat = Coat("P&G", 55)
print(f"Расход ткани на пошив пальто {coat.size} размера = {round(coat.consumption, 2)} м^2")
coat = Coat("АРБ", 48)
print(f"Расход ткани на пошив пальто {coat.size} размера = {round(coat.consumption, 2)} м^2")
suit = Suit("BSD", 2.2)
print(f"Расход ткани на пошив костюма при росте {suit.growth} м. = {round(suit.consumption, 2)} м^2")
suit = Suit("BSD", 1.7)
print(f"Расход ткани на пошив костюма при росте {suit.growth} м. = {round(suit.consumption, 2)} м^2")
print()
print(f"Общий расход ткани на пошив {Clothe._coat} пальто и {Clothe._suit} костюм. = {Clothe._fabric_consumption} м^2")