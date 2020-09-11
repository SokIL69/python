# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

caption = f'Основы языка Python. Урок 5. Домашнее задание 3.\n'
print(caption)

with open("text_3.txt", 'r', encoding="utf-8") as f:
    content = f.read()
    print(f"Содержимое файла: \n{content}\n")
    f.seek(0)

    i = 0
    common_salaty = 0

    print("Сотрудники имеющие доход меньше 20 000 руб.:")
    for line in f:
        line_without_spaces = ' '.join(line.split())  # удаляем лишние пробелы
        new_line = line_without_spaces.split(' ')  # разделяем на слова по пробелам type(new_line) = <class 'list'>
        if float(new_line[1]) < 20000:
            print(f"- {new_line[0]}. Имеет доход {new_line[1]} руб." )

        common_salaty += float(new_line[1])
        i += 1

    print(f"\nСредняя величина дохода всех {i} сотрудников = {(common_salaty/i):.02f}")

