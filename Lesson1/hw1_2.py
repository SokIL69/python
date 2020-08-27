# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

caption = f'Основы языка Python. Урок 1. Домашнее задание 2.\n'
print(caption)

seconds_in_day = 60*60*24 #86400

while True:
    try:
        total_seconds = int(input('Введите необходимое количество секунд: '))
    except:
        print('Нужно ввести целое число!')
    else:
        if (total_seconds > seconds_in_day):
            print(f'В сутках всего {seconds_in_day} секунд.')
            continue
        elif total_seconds < 0:
            print(f'Нужно > 0')
            continue
        break

#begin_value = 3600 * 3 + 60 * 5 + 7

hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60

hours = '0' + str(hours) if hours <10 else hours
minutes = '0' + str(minutes) if minutes < 10 else minutes
seconds = '0' + str(seconds) if seconds < 10 else seconds

print(f'Вы ввели {total_seconds} секунд.')
print(f'Время: {hours}:{minutes}:{seconds}')

