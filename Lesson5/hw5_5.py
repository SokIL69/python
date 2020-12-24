# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

caption = f'Основы языка Python. Урок 5. Домашнее задание 5.\n'
print(caption)

'''
my_list = list(range(10))
my_strig = ' '.join(str(e) for e in my_list)
print(my_strig)
'''
# Создаём (программно) текстовый файл и записывакм в него программно набор чисел, разделенных пробелами.
with open('hw5_5.txt', 'w+', encoding='utf-8') as f:
    f.writelines(' '.join(str(e) for e in list(range(10))))
    f.seek(0)
    print(f"Содержимое созданного файла:\n{f.read()}")

    # Считаем сумму чисел в файле
    f.seek(0)
    content = f.read()
    sum = sum(map(float, content.split(' ')))
    print(f'Сумма чисел файла = {sum}')

