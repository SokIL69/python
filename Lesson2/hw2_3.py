# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

caption = f'Основы языка Python. Урок 2. Домашнее задание 3.\n'
print(caption)

# Реализация через dict
print("3.1 Implemintation with Dictionary")
months = {
    '1':'January',
    '2':'February',
    '3':'March',
    '4':'April',
    '5':'May',
    '6':'June',
    '7':'July',
    '8':'August',
    '9':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}
month_season = {
    '1':'Winter',
    '2':'Winter',
    '3':'Spring',
    '4':'Spring',
    '5':'Spring',
    '6':'Summer',
    '7':'Summer',
    '8':'Summer',
    '9':'Autumn',
    '10':'Autumn',
    '11':'Autumn',
    '12':'Winter'
}

while True:
    month = input(f"Enter month number (1 to 12): ")
    if month.isdigit() == False or int(month) > 12 or int(month) < 1:
        print('You must enter a number between 1 and 12. Please try again.')
    else:
        break

message = f"You have entered month {month}. It's {months[month]}. {month_season[month]}."
print(message)


# Реализация через list
print("\n3.2 Implemintation with List")
months = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
)
seasons = ( 'Winter', 'Spring', 'Summer', 'Autumn')

while True:
    month = input(f"Enter month number (1 to 12): ")
    if month.isdigit() == False or int(month) > 12 or int(month) < 1:
        print('You must enter a number between 1 and 12. Please try again.')
    else:
        break

month = int(month)
if month == 1 or month == 2 or month == 12:
    season = seasons[0]
elif 2 < month < 6:
    season = seasons[1]
elif 5 < month < 9:
    season = seasons[2]
elif 8 < month < 12:
    season = seasons[3]

message = f"You have entered month {month}. It's {months[month-1]}. {season}."
print(message)