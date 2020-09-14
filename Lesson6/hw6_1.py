# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
# в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
import turtle

caption = f'Основы языка Python. Урок 6. Домашнее задание 1.\n'
print(caption)


class TrafficLight:
    # методы класса
    def __init__(self):
        # self.__color = "yellow"  # цвет
        # self.__type = 2  # состояние светофора
        self.__color = "red"  # цвет
        self.__type = 1  # состояние светофора

    def running(self):
        pause_1 = {"red": 7, "yellow": 2, "green": 5}
        # while True:
        for i in range(10):
            # настройка светофора
            if self.__color == "red":
                self.__color = "yellow"
                self.__type = 1
            elif self.__color == "green":
                self.__color = "yellow"
                self.__type = 2
            elif self.__color == "yellow" and self.__type == 1:
                self.__color = "green"
                self.__type = 0
            elif self.__color == "yellow" and self.__type == 2:
                self.__color = "red"
                self.__type = 0
            # рисуем сигнал светофора
            turtle.color(self.__color)
            turtle.begin_fill()
            turtle.circle(100)
            turtle.end_fill()
            # задержка
            sleep(pause_1[self.__color])
            i += 1


# Создаём объект светофор
a = TrafficLight()
a.running()
