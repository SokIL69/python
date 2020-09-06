# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,а в  цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
caption = f'Основы языка Python. Урок 4. Домашнее задание 7.\n'
print(caption)

def fact(n):
    fact = 1
    i = 0
    if n == 0:
        yield 1 , n
    else:
        while i < n:
            i += 1
            fact = fact * i
            yield fact, i

n = 5
if n >= 0:
    for el, i in fact(n):
        print(f"{i}! = {el}")