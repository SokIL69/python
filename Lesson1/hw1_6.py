'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''
caption = f'Основы языка Python. Урок 1. Домашнее задание 6.\n'
print(caption)

try:
    a = int(input("Ведите количество километров которое пробежал спортсмен в 1 день: "))
    b = int(input("Ведите количество километров которое необходимо пробежать: "))
except ValueError:
    print('Необходимо было ввести целое число!')
else:
    i = 0
    distance = a
    full_distance = a
    while True:
        i += 1
        print(f'{i}-й день: {distance:.2f} км. Всего {full_distance:.2f} км.')
        if b - full_distance <= 0:
            result = f'\nОтвет: на {i}-й день спортсмен достиг результата — не менее {b} км.'
            # print(f'За {i} дн. спортсмен пробежал {full_distance} км.')
            print(result)
            break
        # distance = distance * 1.1
        distance *= 1.1
        full_distance += distance
