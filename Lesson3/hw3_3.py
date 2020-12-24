# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

caption = f'Основы языка Python. Урок 3. Домашнее задание 3.\n'
print(caption)

def my_func(num_1, num_2, num_3):
    """Возвращает сумму наибольших двух аргументов из трёхю"""
    my_num = [num_1, num_2, num_3]
    print(f'num_1 = {my_num[0]}\nnum_2 = {my_num[1]}\nnum_3 = {my_num[2]}')
    min_num = my_num[0]
    for num in my_num:
        if num < min_num:
            min_num = num
    my_num.remove(min_num)
    # my_num.remove(min(my_num)) - д.б. реализация без использования f-и min()

    result = 0
    for num in my_num:
        result += num
    return result

print(f'Cумма наибольших из 3-х чисел: {my_func(-5, 4, 10)}\n')


# вариан функции рабочий
def my_func1(*args):
    """
    Принимает неограниченное количество позиционных аргументов и возвращает их сумму,
    за исключением аргумента, имеющего наименьшее значение.
    """
    my_num = list(args)
    my_num.remove(min(my_num))
    result = 0
    for num in my_num:
        result += num

    return result

print(f'Cумма чисел (2,2,3,5,-1) без минимального: {my_func1(2,2,3,5,-1)}\n')