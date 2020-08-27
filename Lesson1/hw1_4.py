# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
caption = f'Основы языка Python. Урок 1. Домашнее задание 4.\n'
print(caption)

while True:
    try:
        number = int(input('Введите целое положительное число: '))
    except:
        print('Нужно ввести целое число!')
    else:
        if number < 0:
            print(f'Нужно положительное число!')
            continue
        break

print(number)

last_num = number % 10
number = number // 10
max_num = last_num

while number:
    next_num = number % 10
    if next_num >= last_num:
        max_num = next_num
        last_num = next_num
    #print(number)
    number = number // 10


print(max_num)

