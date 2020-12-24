# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func() .
caption = f'Основы языка Python. Урок 3. Домашнее задание 6.\n'
print(caption)

#1-вариант
import string
print(string.capwords(input("1-вариант\nEnter a string of multiple words separated by spaces: ")))

#2-вариант через созданную функцию
def int_func(word):
    """Возвращает слово с прописной первой буквой."""
    result = word.capitalize()
    #result = word.lower().title()
    return result

new_line = input("\n2-вариант\nEnter a string of multiple words separated by spaces: ").split(' ')

for i in range(len(new_line)):
    new_line[i] = int_func(new_line[i])

print(' '.join(list(new_line))) # Создаём строку из списка