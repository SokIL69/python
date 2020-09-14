# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
#
# (длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см)
#   * число см толщины полотна.
#
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

caption = f'Основы языка Python. Урок 6. Домашнее задание 2.\n'
print(caption)


class Road:
    # атрибуты класса
    __thickness = 5  # толщина асфальта
    __mass_asphalt = 25  # масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см

    # методы класса
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_param(self):
        print(f'Параметры дороги:\n- длина:{self._length} м.\n- ширина:{self._width} м.\n- толщина: {Road.__thickness} см.')

    def get_mass_of_asphalt(self):
        # return self._length * self._width * Road.__mass_asphalt * Road.__thickness
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна:'
              f' {self._width}м * {self._length}м * {Road.__mass_asphalt}кг * {Road.__thickness}м = {(self._length * self._width * 25 * Road.__thickness)/1000} т\n')


# Создаём экземпляр класса Road
a = Road(5000, 20)
a.road_param()
a.get_mass_of_asphalt()

b = Road(1000, 15)
b.road_param()
b.get_mass_of_asphalt()