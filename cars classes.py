class car_silvia_s14():

    def __init__(self, name, type, cube, twd):
        self.name = name
        self.type = type
        self.cube = cube
        self.twd = twd

    def print_car(self):
        print('эта машина называется', self.name, ' тип', self.type, ' обьем двигателя',
              self.cube, ' трансмисия', self.twd)


car1 = car_silvia_s14('Silvia s14', '"купе"', '2000 кубов', 'awd (полный привод)')
car1.print_car()  # метод


# print(len())  # функция
class car_mark_2():
    def __init__(self, name, type, cube, twd):
        self.name = name
        self.type = type
        self.cube = cube
        self.twd = twd

    def print_car(self):
        print('эта машина называется', self.name, ' тип', self.type, ' обьем двигателя',
              self.cube, ' трансмисия', self.twd)


car2 = car_mark_2('Mark 2', '"седан"', '2000 кубов', 'rwd (задний привод)')
car2.print_car()
