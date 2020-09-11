#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.

caption = f'Основы языка Python. Урок 5. Домашнее задание 7.\n'
print(caption)

dict = {}
dict_full_income = {}
full_income = 0

with open('text_7.txt', 'r', encoding='utf-8') as read_file:
    print(f"Содержимое исходного файла:\n{read_file.read()}")
    read_file.seek(0)
    for i in read_file:
        line_without_spaces = ' '.join(i.split())  # удаляем лишние пробелы
        new_line = line_without_spaces.split(' ')  # разделяем на слова по пробелам type(new_line) = <class 'list'>

        k = len(new_line)
        revenue = float(new_line[k - 2]) # Выручка
        cost = float(new_line[k - 1]) # Издержки
        income = revenue - cost # Доход/Убыток

        # Удаляем лишнее, оставляя название предприятия
        new_line.pop(k - 1)
        new_line.pop(k - 2)
        firm = ' '.join(new_line) # Наименование предприятия

        # Словарь предприятий
        dict[firm] = revenue - cost
        if income >= 0:
            full_income = revenue - cost # без учёта убытков

# Словарь avarage_profit
dict_full_income["average_profit"] = full_income
# Итоговый список
firms = [dict, dict_full_income]

print(f'\nРезультат обработки данных - итоговый список:\n{firms}')


import json
#Сериализация итогового списка в виде json-объекта в файл.
with open('hw5_7.json', 'w', encoding='utf-8') as write_json:
    json.dump(firms, write_json, ensure_ascii=False)

print('\nДесериализация данных из json-файла')
with open('hw5_7.json', 'r', encoding='utf-8') as read_json:
    data = json.load(read_json)

print(data)