# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

caption = f'Основы языка Python. Урок 4. Домашнее задание 2.\n'
print(caption)

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = []
print(f"Иcходный список {source_list}")

# 1-вариант через цикл
print("1-вариант через цикл")
for i in range(len(source_list)):
    if i != 0 and source_list[i] > source_list[i-1]:
        my_list.append(source_list[i])

print(my_list)

# 2-вариант через генератор списка
print("2-вариант через генератор списка")
print([source_list[i] for i in range(len(source_list)) if i != 0 and source_list[i] > source_list[i-1] ])


# тренировка по использованию lambda-функции
my_list.clear()

print("Тренировка по использованию lambda-функции")
#print(list(filter(lambda i: i !=0 and source_list[i] > source_list[i-1], range(len(source_list)))))
for i in range(len(source_list)):
    if i in list(filter(lambda i: i !=0 and source_list[i] > source_list[i-1], range(len(source_list)))):
        my_list.append(source_list[i])

print(my_list)

