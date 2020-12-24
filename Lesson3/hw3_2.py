# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

caption = f'Основы языка Python. Урок 3. Домашнее задание 2.\n'
print(caption)

def get_user_data(**kwargs):
    """Принимает любое количество именнованных параметров о пользователе и печатает информацию о нём."""
    for n, v in kwargs.items():
        print(f"{n}: {v}")

get_user_data(name="Max",sername="Kim",year=2000,city="Perm",email="max@gmail.com",phon="8-956-451-45-45")
