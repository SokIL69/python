# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

caption = f'Основы языка Python. Урок 3. Домашнее задание 4.\n'
print(caption)

# 1-й способ (через использование оператора **)
def my_funct(x, y):
    """
    Программа принимает действительное положительное число x и целое отрицательное число y,
    после чего возвводит число x в степень y.
    """
    return x**y

# 2-й способ (через использование цикла)
def my_funct1(x, y):
    """
    Программа принимает действительное положительное число x и целое отрицательное число y,
    после чего возвводит число x в степень y.
    """
    result = 1
    for n in range(abs(y)):
        result /= x
    return result

while True:
    try:
        x = float(input("Введите действительное число: x = ").replace(',','.'))
    except ValueError as e:
        print(f"Exception - {e}.\nНеобходимо ввести действительное число!")
    else:
        break

while True:
    try:
        y = int(input("Введите целое отрицательное число: y = "))
    except ValueError as e:
        print(f"Exception - {e}.\nНеобходимо ввести отрицательное число!")
    else:
        if y < 0:
            break
        else:
            print(f"Необходимо ввести отрицательное число!")

print(f'1-вариант\n{x} в степени {y}: {x}^{y}={my_funct(x, y)}')
print(f'2-вариант\n{x} в степени {y}: {x}^{y}={my_funct1(x, y)}')