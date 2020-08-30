# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

caption = f'Основы языка Python. Урок 2. Домашнее задание 2.\n'
print(caption)

my_list = []

i = 0
while True:
    el_list = input(f"Введите {i}-й элемент списка: ")
    if el_list != '':
        my_list.append(el_list)
        i += 1
        flag = input("Завершить ввод элементов списка (Y/N): ")
        if flag == 'y' or flag == 'Y' or flag == 'н' or flag == 'Н':
            break

print(f'Начальный список: {my_list}')

# Обмен элементов списка местами
if len(my_list) > 1:
    for i in range(len(my_list)):
        if i % 2 == 0 and i <= len(my_list) - 2:
            my_list_1 = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = my_list_1

print(f'Результат: {my_list}')