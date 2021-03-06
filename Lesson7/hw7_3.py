# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число) или ЯЧЕЕК?
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__()).0
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки
# должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
# разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
#
# Подсказка: подробный список операторов для перегрузки доступен по ссылке
# https://pythonworld.ru/osnovy/peregruzka-operatorov.html.

caption = f'Основы языка Python. Урок 7. Домашнее задание 3.\n'
print(caption)

class Cage: # Класс Клетка

    def __init__(self, count):
        self.count = abs(count)

    def __str__(self):
        return str(self.count)

    def __add__(self, other): # сложение
        """ Осуществляетсложение клеток"""
        return Cage(self.count + other.count)

    def __sub__(self, other): # вычитание
        """ Осуществляет вычитание клеток"""
        if self.count > other.count:
            return Cage(self.count - other.count)
        else:
            print(f"Ошибка вычитания. Количество ячеек в 1-й клетке {self.count} < количества ячеек 2-й клетки {other.count}.")
            #return 0

    def __mul__(self, other):
        """ Осуществляет умножение клеток"""
        return Cage(self.count * other.count)

    def __floordiv__(self, other):
        """" Осуществляет деление клеток"""
        return Cage(self.count // other.count)

    def make_order(self, cells_in_row):
        """ Организует ячейку в ряды """
        if cells_in_row <= self.count:
            list = divmod(self.count, cells_in_row)
            result = ('*'*cells_in_row + '\n')*list[0] + '*'*list[1]
        else:
            result = '*'*self.count
        return result


cage_1 = Cage(7)
cage_2 = Cage(10)
print(cage_1)
print(cage_2)
print(f"Операция сложения: {cage_1 + cage_2}")
print(f"Операция сложения: {cage_1 + cage_2 + cage_2}")
print(f"Операция вычитани: {cage_1 - cage_2}")
print(f"Операция вычитания: {cage_2 - cage_1}")
print(f"Операция умножения: {cage_2 * cage_1}")
print(f"Операция деления: {cage_2 // cage_1}")
print(f"Операция разложения в ряд:\n{cage_2.make_order(15)}")
print(f"Операция разложения в ряд:\n{cage_2.make_order(4)}")
print(f"Операция разложения в ряд:\n{cage_2.make_order(1)}")
