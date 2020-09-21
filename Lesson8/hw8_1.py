# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

caption = 'Основы языка Python. Урок 8. Домашнее задание 1.\n'
print(caption)
 
class MyDate():

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_number(cls, date):
        #print(cls, date)
        try:
            result = [int(_) for _ in date.split('-')]
        except:
            print("Ошибка! Неверный формат даты.")
            return 101 # Ошибка! Неверный формат даты.
        else:
            return result
        

    @staticmethod
    def validation(date):
        date_new = MyDate.date_to_number(date)
        if date_new != 101:
            error = "Дата введена верно."
            if len(date) > 10:
                error = "Ошибка! Неверный формат даты."
            elif date_new[0] > 31 or date_new[0] < 1:
                error = "Ошибка! Введён неправильный день - {date_new[0]}"
                error = "Ошибка! Введён неправильный день - %d" % (date_new[0])
            elif date_new[1] > 12 or date_new[1] < 1:
                error = "Ошибка! Введён неправильный месяц - {date_new[1]}"
                error = "Ошибка! Введён неправильный месяц - %d" % (date_new[1])
            elif date_new[2] > 9999 or date_new[2] < 0:
                error = "Ошибка! Введён неправильный год - {date_new[2]}"
                error = "Ошибка! Введён неправильный год - %d" % (date_new[2])
                
            return error
            


date_1 = MyDate("20-09-2020")
#date_1 = MyDate("20-sep.-2020")
#date_1 = MyDate("32-09-2020")date_1 = MyDate("31-13-2020")
#date_1 = MyDate("31-09-20210")
print(date_1.date)
print(MyDate.date_to_number(date_1.date))
#print("-".join(map(str,MyDate.date_to_number(date_1.date))))
print(MyDate.validation(date_1.date))
