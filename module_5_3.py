'''Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.'''

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(f'Этаж {i}')
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return True

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return True

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return True

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return True

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return True

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        elif isinstance(other, House):
            return House(f'{self.name} и {other.name}', self.number_of_floors + other.number_of_floors)
        else:
            raise TypeError('Нельзя сложить два объекта разных классов')

    def __sub__(self, other):
        if isinstance(other, int):
            if self.number_of_floors >= other:
                return House(self.name, self.number_of_floors - other)
            else:
                raise ValueError('Недостаточно этажей')
        elif isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return House(self.name, self.number_of_floors - other.number_of_floors)
            else:
                raise ValueError('Недостаточно этажей')
        else:
            raise TypeError('Нельзя вычесть два объекта разных классов')

    def __mul__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors * other)
        elif isinstance(other, House):
            return House(f'{self.name} и {other.name}', self.number_of_floors * other.number_of_floors)
        else:
            raise TypeError('Нельзя умножить два объекта разных классов')

    def __div__(self, other):
        if isinstance(other, int):
            if other != 0:
                return House(self.name, self.number_of_floors // other)
            else:
                raise ZeroDivisionError('Деление на ноль')
        elif isinstance(other, House):
            if other.number_of_floors != 0:
                return House(self.name, self.number_of_floors // other.number_of_floors)
            else:
                raise ZeroDivisionError('Деление на ноль')
        else:
            raise TypeError('Нельзя делить два объекта разных классов')

    def __floor__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors // other)
        elif isinstance(other, House):
            return House(f'{self.name} и {other.name}', self.number_of_floors // other.number_of_floors)
        else:
            raise TypeError('Нельзя округлять два объекта разных классов')

    def __mod__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors % other)
        elif isinstance(other, House):
            return House(f'{self.name} и {other.name}', self.number_of_floors % other.number_of_floors)
        else:
            raise TypeError('Нельзя остаток от деления два объекта разных классов')

    def __exp__(self, other):
        if isinstance(other, int):
            return House(self.name, self.number_of_floors ** other)
        elif isinstance(other, House):
            return House(f'{self.name} и {other.name}', self.number_of_floors ** other.number_of_floors)
        else:
            raise TypeError('Нельзя возвести в степень два объекта разных классов')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
