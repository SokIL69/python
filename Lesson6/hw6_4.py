# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
#
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random

caption = f'Основы языка Python. Урок 6. Домашнее задание 4.\n'
print(caption)


class Car:
    # методы класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.state = 0

    def show_param(self):
        print(f"Описание автомобиля:\n- скорость: {0 if self.state == 0 else self.speed} км/час\n"
              f"- цвет: {self.color}\n- марка: {self.name}\n- находится на учёте в полиции: {self.is_police}")

    def go(self):
        print("Автомобиль движется.")
        self.state = 1

    def stop(self):
        print("Автомобиль остановился.")
        self.state = 0

    def turn(self, direction):
        if direction == "left":
            print(f"Автомобиль повернул на лево.")
        else:
            print(f"Автомобиль повернул на право.")

    def show_speed(self):
        if self.state != 0:
            if self.state == 0:
                print(f"Скорость автомобиля 0 км/час.")
            else:
                print(f"Скорость автомобиля {self.speed} км/час.")
        else:
            print(f"Скорость автомобиля 0 км/час.")


class TownCar(Car):

    # методы класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.state = 0
        print('\nАвтомобиль класса "TownCar"')

    def show_speed(self):
        if self.state != 0:
            if self.speed <= 60:
                print(f"Скорость автомобиля {self.speed} км/час.")
            else:
                print(f"Скорость автомобиля ({self.speed} км/час) превысила разрешённые 60 км/час.")
        else:
            print(f"Скорость автомобиля 0 км/час.")


class SportCar(Car):

    # методы класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.state = 0
        print('\nАвтомобиль класса "SportCar"')


class WorkCar(Car):

    # методы класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.state = 0
        print('\nАвтомобиль класса "WorkCar"')

    def show_speed(self):
        if self.state != 0:
            if self.speed <= 40:
                print(f"Скорость автомобиля {self.speed} км/час.")
            else:
                print(f"Скорость автомобиля ({self.speed} км/час) превысила разрешённые 40 км/час.")
        else:
            print(f"Скорость автомобиля 0 км/час.")


class PoliceCar(Car):

    # методы класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.state = 0
        print('\nАвтомобиль класса "PoliceCar"')


direction = ['left', 'right']

a = TownCar(80, "black", "Lada", False)
a.show_param()
# выполняем прямой доступ к параметрах объекта
print(a.speed, a.color, a.name, a.is_police, sep="; ")
# вызываем методы объекта
a.go()
a.show_param()
a.show_speed()
# поворачиваем
a.turn(random.choice(direction))
a.turn(random.choice(direction))
a.turn(random.choice(direction))
a.turn("left")
a.turn("right")
a.stop()
a.show_speed()

b = WorkCar(40, "black", "Lada", False)
b.show_param()
b.go()
b.show_param()
b.show_speed()
b.turn("left")
b.turn("right")
b.stop()
b.show_speed()

c = SportCar(120, "black", "Lada-vesta", True)
c.show_param()
c.go()
c.show_param()
c.show_speed()
c.turn("left")
c.turn("right")
c.stop()
c.show_speed()

