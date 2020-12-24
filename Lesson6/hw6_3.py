# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. (wage - заработная плата)
#
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

caption = f'Основы языка Python. Урок 6. Домашнее задание 3.\n'
print(caption)


class Worker:

    # конструктор класса
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position   # должность
        if position == "инженер":
            self._income = {"wage": 30000, "bonus": 3000}
        elif position == "рабочий":
            self._income = {"wage": 25000, "bonus": 1500}
        else:
            self._income = {"wage": 20000, "bonus": 500}


class Position(Worker):
    # методы класса
    def get_full_name(self):
        print(f'{self.surname} {self.name}, {self.position}')

    def get_total_income(self):
        print(f'Доход с учётом премии: {self._income["wage"] + self._income["bonus"]} руб.\n')


# создаём экземпляры класса
a = Position("Иван", "Иванов", "инженер")
# проверяем доступ к параметрам класса
print(a.name, a.surname, a.position, sep=" - ")
# вызываем методы класса
a.get_full_name()
a.get_total_income()

b = Position("Степан", "Степанов", "рабочий")
b.get_full_name()
b.get_total_income()

с = Position("Пётр", "Петров", "экономист")
с.get_full_name()
с.get_total_income()