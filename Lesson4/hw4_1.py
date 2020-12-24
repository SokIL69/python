# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

caption = f'Основы языка Python. Урок 4. Домашнее задание 1.\n'
print(caption)

# tab_N - Табельный номер
# month - номер месяца
# production_in_hours - выработка в часах (час.)
# rate_per_hour - ставка в час (руб.)
# premium - премия (руб.)
# name, tab_N, production_in_hours, rate_per_hour, premium = argv

months = {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}
employees = (
    {"Табельный номер": "0001", "ФИО": "Иванов И.В."},
    {"Табельный номер": "0002", "ФИО": "Петров П.П."},
    {"Табельный номер": "0003", "ФИО": "Сидоров А.В."},
)

def salary(production_in_hours, rate_per_hour, premium):
    """Начисляет заработную плату

    Именованные параметры:
    production_in_hours - выработка в часах (час.)
    rate_per_hour - ставка в час (руб.)
    premium - премия (руб.)

    """
    return (production_in_hours * rate_per_hour) + premium

def help():
    print(f"Справка:\n1. Для начисления з\п наберите команду: hw4_1.py tab_N month production_in_hours rate_per_hour premium\n" +
          f"    - tab_N - табельный номер,\n" +
          f"    - month - месяц,\n" +
          f"    - production_in_hours - выработка в часах (час.),\n" +
          f"    - rate_per_hour - ставка в час (руб.),\n" +
          f"    - premium - премия (руб.)\n" +
          f"    Пример: hw4_1.py 0001 12 45.5 15.5 400\n" +
          f"2. Для получения списка сотрудников наберите: hw4_1.py list")

def error():
    print(f"Error!\nМесяц, выработка в часах, ставка в час и премия должны быть числами!\n\n" +
          f"Для начисления з\п наберите команду: hw4_1.py tab_N production_in_hours rate_per_hour premium\n" +
          f"Пример: hw4_1.py 0001 12 45.5 15.5 400\n" +
          f"Для получения списка сотрудников наберите: hw4_1.py list\?" +
          f"Для получения справки по команде набирите: hw4_1.py ?")


if argv[1] == "list":
    for i in employees:
        print(f'{i["ФИО"]}: табельный № {i["Табельный номер"]}.')
elif argv[1] == "?":
    help()
else:
    try:
        tab_N = argv[1]
        month = int(argv[2])
        production_in_hours = float(argv[3])
        rate_per_hour = float(argv[4])
        premium = float(argv[5])
    except:
        error()
    else:
        if 1 <= month <= 12:
            i = 0
            for employee in employees:
                if employee["Табельный номер"] == tab_N:
                    print(f'{employee["ФИО"]} (табельный № {employee["Табельный номер"]}):' +
                          f' начислена заработная плата за {months[month]} =' +
                          f' {salary(production_in_hours, rate_per_hour, premium):02} руб.')
                    break
                i += 1

            if i == len(employees):
                print(f"Неверно введён табельный номер сотрудника!\n" +
                      f"Для получения списка сотрудников наберите: hw4_1.py list")
        else:
            print("Неверно введён номер месяца!")