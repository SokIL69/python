# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
caption = f'Основы языка Python. Урок 1. Домашнее задание 3.\n'
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

print(f'Вы ввели число {number}')

result = number + int(f'{number}{number}') + int(f'{number}{number}{number}')
print(f'{number} + {number}{number} + {number}{number}{number} = {result}')