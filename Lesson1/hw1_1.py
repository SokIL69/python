# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите
#    у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

caption = f'Основы языка Python. Урок 1. Домашнее задание 1.\n'
print(caption)

while True:
    name = input('Введите ваше имя: ')
    if not name.strip(): # Чтоб не пропускать строку "   "
        print('Вы забыли ввести ваше имя!')
        continue
    else:
        break

while True:
    try:
        age = int(input('Введите ваш возраст: '))
    except:
        print('Нужно ввести целое число!')
    else:
        if 0 > age or age > 100:
            print('Не может быть! Повторите.')
            continue
        break

print(f'\nПривет {name}, вам {age} лет.\n')

while True:
    try:
        int_num = int(input('Введите целое число: '))
    except:
        print('\nНужно ввести целое число!')
    else:
        print(f'Вы ввели: {int_num}')
        break

while True:
    try:
        flt_num = float(input('\nВведите действительное число: '))
    except:
        print('Нужно ввести действительное число!')
    else:
        print(f'Вы ввели: {flt_num}')
        break




