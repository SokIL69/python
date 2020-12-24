# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

caption = f'Основы языка Python. Урок 3. Домашнее задание 1.\n'
print(caption)

def dividing(num_1, num_2):
    """Выполняет деление двух чисел. Обрабатывается исключение ZeroDivisionError."""
    try:
        result = num_1/num_2
    except ZeroDivisionError as e:
        print(f"Exception - {e} (деление на 0).")
    except TypeError as e:
        print(f"Exception - {e}.")
    else:
        print(f'{num_1}/{num_2} = {result}')

while True:
    try:
        num_1 = float(input("\nВведите числитель дроби: a = ").replace(',','.'))
        num_2 = float(input("Введите знаменатель дроби: b = ").replace(',','.'))
    except ValueError as e:
        print(f"Exception - {e}.\nНеобходимо ввести число!")
    else:
        break

dividing(num_1, num_2)



# dividing() - без параметров даёт исключение TypeError