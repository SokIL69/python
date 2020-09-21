# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

caption = 'Основы языка Python. Урок 8. Домашнее задание 7.\n'
print(caption)


class MyComplex():

    def __init__(self, real, cmplx):
        self.real = real
        self.cmplx = cmplx

    def __str__(self):
         """ Отображает комплексное число """

         #print(f"{self.real} + i * {self.cmplx}")
         return "%d + i*%d" % (self.real, self.cmplx)

    def __add__(self, other):
        """ Сложение комплексных чисел """
        
        return MyComplex(self.real + other.real, self.cmplx + other.cmplx)


    def __mul__(self, other):
        """ Умножение комплексных чисел """
        #(a + i*b)(c + i*d) = (ac - bd) + i(ad + bc) # i^2 = -1, i = sqrt(-1)- мнимая единица
        return MyComplex(self.real * other.real - self.cmplx * other.cmplx,
                         self.real * other.cmplx + other.real * self.cmplx)

    
complex_1 = MyComplex(1, 2)
complex_2 = MyComplex(3, 4)
complex_3 = MyComplex(-1, 1)

print(complex_1)
print(complex_2)
print(complex_3)

print("Сложение комплексных чисел:")
print(f"({complex_1}) + ({complex_2}) = {complex_1 + complex_2}")
#print(complex_1 + complex_2)
print(f"({complex_1}) + ({complex_2}) + ({complex_3}) = {complex_1 + complex_2 + complex_3}")
#print(complex_1 + complex_2 + complex_3)
print("Умножение комплексных чисел:")
print(complex_1 * complex_2)
print(f"({complex_1}) * ({complex_2}) = {complex_1 * complex_2}")
print("Смешанная операция над комплексных чисел:")
print(f"({complex_1}) * ({complex_2}) + ({complex_3}) = {complex_1 * complex_2 + complex_3}")
#print(complex_1 * complex_2 + complex_3)

