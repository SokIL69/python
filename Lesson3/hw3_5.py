# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

caption = f'Основы языка Python. Урок 3. Домашнее задание 5.\n'
print(caption)

def sum_list(list):
    list_1 = []
    for n in list:
        try:
            float(n)
        except:
            continue
        else:
            list_1.append(n)
        #if n.isnumeric():
        #    list_1.append(n)

    print(f'В вашей строке содержатся следующие числа: {list_1}')
    list_1 = [float(elem) for elem in list_1]
    return sum(list_1)

line = ""
while True:
    line_1 = input("Введите строку чисел разделённых пробелом (для завершения ввода введите q): ")
    index = line_1.find("q")
    if index != -1:
        line += line_1[:index]
        break
    else:
        line += " " + line_1


print('Your enter a strig:"' + line + '"\n')

line_without_spaces = ' '.join(line.split())  # удаляем лишние пробелы
new_line = line_without_spaces.split(' ')  # разделяем на слова по пробелам

print(f"Сумма чисел строки = {sum_list(new_line)}")