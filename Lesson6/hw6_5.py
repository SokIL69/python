# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

caption = f'Основы языка Python. Урок 6. Домашнее задание 5.\n'
print(caption)


class Stationery:

    def __init__(self, title):
        self.title = title

    def show_param(self):
        print(f"\nОписание товара: {self.title}")

    def draw(self):
        print("Запуск отрисовки: Stationery.")



class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки: Pen.")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки: Pencil.")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки: Handle.")


a = Stationery("Parent")
a.show_param()
a.draw()

b = Pen("Pen_1")
b.show_param()
b.draw()

c = Pencil("Pencil_1")
c.show_param()
c.draw()

d = Handle("Pencil_1")
d.show_param()
d.draw()

