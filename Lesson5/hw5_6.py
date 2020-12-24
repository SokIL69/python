 # 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
 # и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
 # Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 # Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
 # Вывести словарь на экран.
 # Примеры строк файла:
 # Информатика: 100(л) 50(пр) 20(лаб).
 # Физика: 30(л) — 10(лаб)
 # Физкультура: — 30(пр) —
 #
 # Пример словаря:
 # {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

caption = f'Основы языка Python. Урок 5. Домашнее задание 6.\n'
print(caption)

from itertools import groupby

def number_from_strinf(text):
    """ Возвращеем числа из строки символов

    :param text: исходная строка
    :return: итератор по сгруппированным элементам переданного объекта -> list
    """
    return [int(''.join(str)) for is_digit, str in groupby(text, str.isdigit) if is_digit]

dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    print(f"Содержимое исходного файла:\n{f.read()}")
    f.seek(0)
    for i in f:
        # Находим название предмета
        n = i.find(':')
        subject = i[:n]
        # Поиск чисел в строке
        #l = [int(''.join(i)) for is_digit, i in groupby(i, str.isdigit) if is_digit]
        l = number_from_strinf(i)
        #print(l)
        # Добавляем новый элемент в словарь
        dict[subject] = sum(map(int, l))

print(f'\nРезультат обработки:\n{dict}')

# Пример использование функции фильтр
a = [1, -4, 6, 8, -10]
def func(x):
     if x > 0:
             return 1
     else:
             return 0

b = filter(func, a)
b = list(b)
#print(b)


# Поиск чисел в строке
my_str = "hello 12 hi 89"
l = [int(''.join(i)) for is_digit, i in groupby(my_str, str.isdigit) if is_digit]
#print(l)
