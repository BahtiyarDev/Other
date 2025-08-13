# Inheritance - Нследование
# Dog [is] animal

# Compositions - Композиция
# Dog [has] tail

# Унификакция - обобщенеи поведения - Polymorphism

# ООП где лучше использовать?
# большие игры
# глобальные сущности вроде банкинга

# ООП где лучше избегать?
# для мимнимальной логики
# когда уже етсь подобный встроенный функционал

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.__hp = 100
        self.__name = name

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self):
        self.__hp += 20
        return f'{self.__name} довольно кушает'

    def move(self):
        self.__hp -= 20
        return f'{self.__name} идет'

    def get_hp(self):
        return self.__hp

    def get_name(self):
        return self.__name


class Lion(Animal):
    def make_sound(self):
        return f'{self.get_name()} рычит'


class Parrot(Animal):
    def make_sound(self):
        return f'{self.get_name()} чирикает'


class Penguin(Animal):
    def make_sound(self):
        return f'{self.get_name()} крякает'


class Elephant(Animal):
    def make_sound(self):
        return f'{self.get_name()} дует в хобот'


class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_actions(self):
        for animal in self.animals:
            print(animal.make_sound())
            print(animal.move())

    def get_name(self):
        return self.name


class Zoo:
    def __init__(self):
        self.enclosures = []

    def add_enclosure(self, name_enclosure):
        self.enclosures.append(name_enclosure)

    def simulate(self):
        for enclosure in self.enclosures:
            enclosure.list_actions()

    def feed_all(self):
        for enclosure in self.enclosures:
            for animal in enclosure.animals:
                print(animal.feed())

    def accept_visitors(self, visitor_list):
        for visitor in visitor_list:
            if visitor.get_ticket():
                for enclosure in self.enclosures:
                    print(visitor.get_in(enclosure))


class ZooKeeper:
    def feed_all(self, zoo):
        zoo.feed_all()


class Ticket:
    def __init__(self, visitor_name, enclosures_name):
        self.visitor_name = visitor_name
        if isinstance(enclosures_name, str):
            self.enclosures_name = [enclosures_name]
        else:
            self.enclosures_name = enclosures_name

    def get_visitor_name(self):
        return self.visitor_name

    def get_enclosures(self):
        return self.enclosures_name

    def can_access(self, enclosure):
        if enclosure in self.enclosures_name:
            return True
        else:
            return False


class Visitor:
    def __init__(self, name, ticket):
        self.name = name
        self.ticket = ticket
        self.visited_enclosures = []

    def get_ticket(self):
        return self.ticket

    def get_name(self):
        return self.name

    def get_in(self, enclosure):

        if self.ticket.can_access(enclosure.get_name()):
            self.visited_enclosures.append(enclosure.get_name())
            return f'Доступ для {self.name} в {enclosure.get_name()} разрешен'
        else:
            return f'Доступ для {self.name} в {enclosure.get_name()} запрещен'

    def get_report(self):
        return f'{self.name} посетил(-a) {self.visited_enclosures}'


ticket1 = Ticket('Alice', ['animals', 'birds'])
# print(ticket1.get_visitor_name())
# print(ticket1.get_enclosures())


visitor1 = Visitor('Alice', ticket1)
# print(visitor1.get_in('enclosure1'))
# print(visitor1.get_in('enclosure2'))

ticket2 = Ticket('Bob', 'mix')
visitor2 = Visitor('Bob', ticket2)


lion1 = Lion('Lion1')
penguin1 = Penguin('penguin1')
elephant1 = Elephant('elephant1')
parrot1 = Parrot('parrot1')

enclosure1 = Enclosure('birds')
enclosure2 = Enclosure('animals')
enclosure3 = Enclosure('mix')


enclosure1.add_animal(penguin1)
enclosure1.add_animal(parrot1)

enclosure2.add_animal(lion1)
enclosure2.add_animal(elephant1)

enclosure3.add_animal(elephant1)
enclosure3.add_animal(parrot1)
enclosure3.add_animal(lion1)


zoo = Zoo()
zoo.add_enclosure(enclosure1)
zoo.add_enclosure(enclosure2)
zoo.add_enclosure(enclosure3)

zoo.accept_visitors([visitor1, visitor2])

print(visitor1.get_report())
print(visitor2.get_report())

# zoo.simulate()

# # # print(lion1.feed())

# zookeeper = ZooKeeper()
# zookeeper.feed_all(zoo)

# print(lion1.get_hp())
# print(lion1.move())
# print(lion1.move())
# print(lion1.get_hp())
# print(lion1.feed())
# print(lion1.get_hp())


# Рефактринг - переписать код и оптимизировать его, в идеале писать правильный код сразу, но иногда можноо написать функционал как есть, а потом отрефакторить
