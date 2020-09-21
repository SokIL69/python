# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

caption = 'Основы языка Python. Урок 8. Домашнее задание 4, 5, 6.\n'
print(caption)


class Warehouse:  # Office equipment warehouse (скдад)

    i = 0  # № последней операции по принятию оргтехники на склад
    goods = []
    #feature = {'оборудование': '', 'производитель': '', 'название': '', 'количество': ''}
    j = 0  # № последней операции по выдаче оргтехники в подразделение
    sectors = []
    #branch = {'подразделение': '', 'оборудование': '', 'название': '', 'количество': ''}

    def getting(self, equipment, count):
        # Приём товара
        #self.feature = {"оборудование": equipment.equipment_type, "производитель": equipment.brend,
        #                "название": equipment.name, "количество": count}
        self.i += 1
        #self.goods.append((self.i, self.feature))
        self.goods.append((self.i, equipment, count))

    def moving(self, branch, equipment, count):
        # Выдача товара
        if branch == 1:
            branch_new = 'бухгалтерия'
        elif branch == 2:
            branch_new = 'отдел кадров'
        else:
            branch_new = 'администрация'

        #self.branch = {'подразделение': branch_new, 'оборудование': equipment.equipment_type,
        #               'название': equipment.name, 'количество': count}
        self.j += 1
        #self.sectors.append((self.j, self.branch))
        self.sectors.append((self.j, branch_new, equipment, count))

    def get_print(self):
        print('\nПринято на склад:')
        for _ in range(len(self.goods)):
            #print(self.goods[_])
            print(f'{self.goods[_][0]}\tОборудование: {self.goods[_][1].equipment_type}\t'
                  f'Количество: {self.goods[_][2]}\t'
                  f'Производитель: {self.goods[_][1].brend}\t'
                  f'Название: {self.goods[_][1].name}\t')
        print()

    def move_print(self):
        print('\nВыдано в подразделения:')
        for _ in range(len(self.sectors)):
            #print(self.sectors[_])
            print(f'{self.sectors[_][0]}\tПодразделение: {self.sectors[_][1]}\t'
                  f'Оборудование: {self.sectors[_][2].equipment_type}\t'
                  f'Количество: {self.sectors[_][3]}\t'
                  f'Производитель: {self.sectors[_][2].brend}\t'
                  f'Название: {self.sectors[_][2].name}\t')


class Equipment:  # Office equipment (оборудование)

    def __init__(self, brend, name, price):
        self.brend = brend
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class Printer(Equipment):

    def __init__(self, brend, name, price, print_type, technology, speed):
        # printing_type: 1 - черно-белый, 2 - цветной
        # technology: 1 - лазерный, 2 - струйный
        # speed 20 стр/мин

        super().__init__(brend, name, price)
        self.equipment_type = 'принтер'
        self.print_type = print_type
        self.technology = technology
        self.speed = speed


class Scanner(Equipment):

    def __init__(self, brend, name, price, scanner_type, color, max_format):
        # Оптическое разреш. сканера: 4800x4800 т/д
        # max_format (Размер документа): 0-A3,1-А4, 2-A5
        # scanner_type (Тип сканера): 1 - планшетный
        # color (Цвет): чёрный/белый

        super().__init__(brend, name, price)
        self.equipment_type = 'сканер'
        self.scanner_type = scanner_type
        self.color = color
        self.max_format = max_format


class Xerox(Equipment):

    def __init__(self, brend, name, price, technology, max_format, speed):
        # technology (технология печати): 1-лазерный
        # max_format(формат): 0-A3, 1-А4
        # (скорость): 25 стр/мин
        # (разрешение сканирования): 1-600×600 dpi, 2- 300×300 dpi

        super().__init__(brend, name, price)
        self.equipment_type = 'ксерокс'
        self.technology = technology
        self.max_format = max_format
        self.speed = speed

i = 0
equipment = []
a = Printer("BROTHER", "Brother HL-1110R", 8500, 1, 1, 20)
b = Scanner("Canon", "CanoScan LiDE400", 6390, 1, "black", 1)
c = Xerox("CANON", "CANON imageRUNNER C3125i", 116430, 1, 1, 25)
print(a)
print(b)
print(c)
print()

equipment.append((i + 1, a))
equipment.append((i + 2, b))
equipment.append((i + 3, c))

print(f'Позиция\t Оборудование')
for _ in range(len(equipment)):
    print(f'{equipment[_][0]}\t {equipment[_][1].__dict__}')

print()

s = Warehouse()
# Приём на склад:
#s.getting(a, 10)
#s.getting(b, 5)
#s.getting(c, 5)
while True:
    try:
        position = input(f'Введите № позиции товара которого нужно принять на складе.'
                         f'Для вывода списка товаров нажмите "l". Для выхода нажать "q": ')
        if position.lower() == 'l' or position.lower() == 'д':
            print(f'Позиция\t Оборудование')
            for _ in range(len(equipment)):
                print(f'{equipment[_][0]}\t {equipment[_][1].__dict__}')
            continue

        if position.lower() == 'q' or position.lower() == 'й':
            break
        else:
            number = int(input(f'Введите количество товара которого нужно принять на складе. Для выхода нажать "q": '))
            for _ in range(len(equipment)):
                if equipment[_][0] == int(position):
                    #print(f'{equipment[_][0]}\t {equipment[_][1].__dict__}')
                    s.getting(equipment[_][1], number)

    except:
        print("Error! введена неправильная информация. Повторите попытку!")
        continue

#Принято на склад:
s.get_print()

# Выдача в подразделения:
# s.moving('администрация', 'Xerox', 'CANON imageRUNNER C3125i', 1)
#s.moving(1, a, 3)
#s.moving(2, a, 2)
#s.moving(3, a, 1)
while True:
    try:
        position = input(f'Введите № позиции товара которого нужно передать в подразделение.\n'
                         f'Для вывода списка товаров на складе нажмите "l". Для выхода нажать "q": ')
        if position.lower() == 'l' or position.lower() == 'д':
            s.get_print()
            continue
        if position.lower() == 'q' or position.lower() == 'й':
            break
        else:
            if int(position) < 1 or int(position) > s.i:
                print(f'Введена неправильная позиция товара на складе! Позиция товара > 0 и < {s.i}.')
                continue
            else:
                branche = input(f'Введите № подразделения (1-бухгалтерия, 2-отдел кадровб 3-администрация). Для выхода нажать "q": ')
                if branche.lower() == 'q' or branche.lower() == 'й':
                    break
                else:
                    number = int(input(f'Введите количество товара которого нужно передать в подразделение. Для выхода нажать "q": '))
                    for _ in range(len(equipment)):
                        if equipment[_][0] == int(position):
                            s.moving(int(branche), equipment[_][1], number)
    except:
        print("Error! введена неправильная информация. Повторите попытку!")
        continue

print()
#Выдано в подразделения:
s.move_print()