# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

caption = f'Основы языка Python. Урок 7. Домашнее задание 1.\n'
print(caption)


class Matrix:
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.columns = 1
        # Определяем размерность матрици и заполняем недостающие элементы 0-ми
        try:
            for i in range(self.rows):
                for j in range(len(matrix[i])):
                    if self.columns <= len(matrix[i]):
                        self.columns = len(matrix[i])
            for i in range(self.rows):
                for j in range(self.columns):
                    try:
                        matrix[i][j]
                    except:
                        matrix[i].append(0)
        except:
            pass
        self.matrix = matrix

    def __str__(self):
        """ Отображает элементы матрицы """

        print_matrix = ''
        for i in range(len(self.matrix)):
            try:
                # если матрица двухмерная (n x m)
                len(self.matrix[i])
                for j in range(len(self.matrix[i])):
                    print_matrix += str(self.matrix[i][j]) + ' '
                print_matrix += '\n'
            except:
                # если матрица одномерная (вектор)
                print_matrix += str(self.matrix[i]) + ' '

        return print_matrix

    def __add__(self, other):
        """ Сложение матриц. Складывать можно только матрицы одной размерности. """
        matrix = []
        list_1 = []
        if (self.rows == other.rows and self.columns == other.columns):
            try:
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        list_1.append(self.matrix[i][j] + other.matrix[i][j])
                    matrix.append([])
                    for k in range(len(list_1)):
                        matrix[i].append(list_1[k])
                    list_1.clear()
            except:
                matrix.clear()
                #print("Ошибка сложения! Матрицы должны быть одной размерности.")
        else:
             print("Ошибка сложения! Матрицы должны быть одной размерности.")

        return Matrix(matrix)


# Вектор-строка
matrix_0 = Matrix([[1,2]])
# Вектор-столбец
matrix_01 = Matrix([[1],[2]])

# Матрица размерности 3 x 3
matrix_1 = Matrix([[1,2,100],[3,4],[5,6]])
# Матрица размерности 3 x 3
matrix_12 = Matrix([[7,8],[9,10],[11,12,100]])

# Матрица размерности 3 x 3
matrix_2 = Matrix([[7,8],[9,10],[11,12]])

print(f"Размерность матрицы {matrix_0.rows} x {matrix_0.columns}" )
print(matrix_0)
print(f"Размерность матрицы {matrix_01.rows} x {matrix_01.columns}" )
print(matrix_01)
print(f"Размерность матрицы {matrix_1.rows} x {matrix_1.columns}" )
print(matrix_1)
print(f"Размерность матрицы {matrix_12.rows} x {matrix_12.columns}" )
print(matrix_12)

print("Сложение матриц:")
print(matrix_1 + matrix_12)

print(f"Размерность матрицы {matrix_2.rows} x {matrix_2.columns}" )
print(matrix_2)

print("Сложение матриц разной размерности:")
print(matrix_0 + matrix_2)

