# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

caption = f'Основы языка Python. Урок 2. Домашнее задание 1.\n'
print(caption)

# Создаём переменную типа 'Исключение'
try:
    print(0 / 0)
except ZeroDivisionError as e:
    exp = e

list_dif_types = [123, 'Hello', 45.1, True, [1, 2, 3], ('a', 'b', 'c'), {'name': 'Ivan', 'age': 18}, None, {1, 2, 3},
                  exp, b'bytes', bytearray(b'hello world!')]

for list_dif_type in list_dif_types:
    print(type(list_dif_type))
