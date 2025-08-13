# Полиморфизм - это наличие одинаковых методов у разныхклассов, но с разной реализацией

# class Animal:
#     def __init__(self):
#         pass

#     def speak(self):
#         pass

# class Cat(Animal):
#     def speak(self):
#         print('meow')


# class Dog(Animal):
#     def speak(self):
#         print('raf')

# animals = [Cat(), Dog()]

# for animal in animals:
# animal.speak()


# fly: airplane, bird; fly = None for human


# Виды полиморфизма:
# ad-hoc - перегрузка методов(перезапись функционала ситуационно)
# подтипов - наследование методов родителя и разная реализация внутри себя
# типов данных - зависимо от переданных данных разная реализация, к примеру(list[int] | list[str])


# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r**2


# class Square:
#     def __init__(self, a):
#         self.a = a

#     def area(self):
#         return self.a**2


# class Triangle:
#     def __init__(self, c, h):
#         self.c = c
#         self.h = h

#     def area(self):
#         return (self.c * self.h)/2


# shapes = [Square(4), Circle(2), Triangle(7, 3)]

# def total_area(shapes):
#     total = 0
#     for shape in shapes:
#         total += shape.area()

#     return total

# print(total_area(shapes))


# class Warrior:
#     def __init__(self):
#         pass

#     def attack(self):
#         return 'Удар мечом!'


# class Mage:
#     def __init__(self):
#         pass

#     def attack(self):
#         return 'Удар магией!'


# class Archer:
#     def __init__(self):
#         pass

#     def attack(self):
#         return 'Выстрел луком!'

# units = [Warrior(), Mage(), Archer()]

# def battle(units):
#     for unit in units:
#         print(unit.attack())

# # (unit.attck() for unit in units)

# battle(units)


# class Add:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def calculate(self):
#         return self.a + self.b

# class Substract:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def calculate(self):
#         return self.a - self.b

# class Multiply:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def calculate(self):
#         return self.a * self.b


# operations = [Add(4, 6), Substract(4, 6), Multiply(4, 6)]

# def perform_operations(operations):
#     for operation in operations:
#         print(operation.calculate())


# perform_operations(operations)


# Абстаркция - сборка классов, используя самые важные свойства, игнорируя детали

from abc import ABC, abstractmethod


# class Transport(ABC):

#     @abstractmethod
#     def drive(self):
#         pass

#     @abstractmethod
#     def start_engine(self):
#         pass


# class Car(Transport):
#     def __init__(self):
#         self.age = 0

#     def drive(self):
#         print('Машина едет')

#     def start_engine(self):
#         print('Машина запустила двигатель')


# class Bike(Transport):
#     def __init__(self):
#         self.age = 0

#     def drive(self):
#         print('Велик едет')

#     def start_engine(self):
#         print('У велика нет двигателя')


# car = Car()
# bike = Bike()

# print(bike.drive())
# print(bike.start_engine())

# # Композиция - сборка класса на основе других простых и независимых классов


# class CPU:
#     def __init__(self, model):
#         self.model = model


# class RAM:
#     def __init__(self, memorie):
#         self.memorie = memorie


# class Computer:
#     def __init__(self, cpu, ram):
#         self.cpu = CPU(cpu)
#         self.ram = RAM(ram)

#     def comp_specs(self):
#         print(f'This computer has {self.cpu.model} and ram {self.ram.memorie}')


# comp1 = Computer('Intel Core I9', '16GB')
# comp1.comp_specs()

# Плюс клмпозиции перед наследованием в том, чтотподклассы независимы от родительского класса


# class Gadget(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def get_info(self):
#         pass

# class Smartphone(Gadget):
#     def __init__(self, name):
#         self.name = name
        

#     def turn_on(self):
#         print(f'{self.name} включился ')

#     def get_info(self):
#         print(f'Тип: Smartphone, Модель: {self.name}')

# class Smartwatch(Gadget):
#     def __init__(self, name):
#         self.name = name
        

#     def turn_on(self):
#         print(f'{self.name} включился ')

#     def get_info(self):
#         print(f'Тип: Smartwatch, Модель: {self.name}')

# smartphone = Smartphone('Iphone 15')
# smartphone.turn_on()
# smartphone.get_info()

# smartwatch = Smartwatch('Iwatch 15')
# smartwatch.turn_on()
# smartwatch.get_info()

