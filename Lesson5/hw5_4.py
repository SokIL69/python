# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

caption = f'Основы языка Python. Урок 5. Домашнее задание 4.\n'
print(caption)

def text_replace(str):
    """ Заменняет в строке английские числительные на русские.

    :param str: исходная строка
    :return: string
    """
    numbers = ['One', 'Two', 'Three', 'Four', '...']
    numbers_rus = ['Один', 'Два', 'Три', 'Четыре', 'и т. д.']
    for i in range(len(numbers)):
        if str.find(numbers[i]) != -1:
            str = str.replace(numbers[i], numbers_rus[i])
            break
    return str


with open('text_4.txt', 'r', encoding='utf-8') as source_file:
    content = source_file.read()
    print(f'Cодержимое исходного файла:\n{content}', end='\n\n')

    # Читаем построчно файл, заменяем английские числительные на русские и записываем строку в новый файл.
    with open('text_4_new.txt', 'r+', encoding='utf-8') as new_file:
        for i in source_file:
            #запись строк в new_file
            print(text_replace(i), file=new_file)
        new_file.seek(0)
        print(f'Cодержимое нового файла:\n{new_file.read()}')


