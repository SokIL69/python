# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

caption = 'Основы языка Python. Урок 8. Домашнее задание 2.\n'
print(caption)

class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt
        

in_data = input("Введите знаменатель дроби: ")

try:
    in_data = int(in_data)
    if in_data == 0:
        raise OwnError("Error! Деление на ноль.")
    result = 100 / in_data
except (ValueError, OwnError) as err:
    print(err)
else:
    print("100/(%d) = %f" % (in_data, 100/in_data))
    #print(f"100/{in_data} = {100/in_data}")
    
 
