# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

caption = f'Основы языка Python. Урок 2. Домашнее задание 4.\n'
print(caption)

goods = []
flag = input('Для использования тестового примера нажмите - 1, для ручного ввода товаров  - любую клавишу: ')

if flag == '1' or flag == '!':
    # Тестовый пример
    line = "             Пользователь     вводит   строку  из   нескольких   слов,   разделённых   пробелами.  "
else:
    line = input(f"Enter a string of multiple words separated by spaces: ")

line_without_spaces = ' '.join(line.split()) # удаляем лишние пробелы
new_line = line_without_spaces.split(' ') # разделяем на слова по пробелам

print('Your enter a strig:\n"' + line + '"\n')

print('Result:')
for i in range(len(new_line)):
    print(f'{i+1} - {new_line[i][:10]}')