class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id


# Create an object of the superclass
person = Person("John", 25)
print(person.get_info())  # 'John is 25 years old.'
# Create an object of the subclass
student = Student("Leo", 20, 10035464)
print(student.get_info())  # 'Leo is 20 years old.'
print(student.get_id())  # 10035464


# Single parent - Single inheritance
class Parent:
    def say_hi(self):
        return "Hello!"


class Child(Parent):
    def go_school(self):
        return "I go to school."


child = Child()
print(child.say_hi())  # Hello!
print(child.go_school())  # I go to school.


# Multiple Inheritance - Father and Mother, Daughter inherits both
class Father:
    def __init__(self):
        self.father_name = 'Taylor Evans'


class Mother:
    def __init__(self):
        self.mother_name = 'Bet Williams'


class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'


child = Daughter()
print(child.get_parent_info())  # Father: Taylor Evans, Mother: BetWilliams


# Multilevel Inheritance, any depth - Child becomes Parent -> Granddad - Parent - Child
class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def get_address(self):
        return self.address


grand_child = GrandChild("Grand Name", 19, "Address 15-17")
print(grand_child.name)  # Grand Name
print(grand_child.age)  # 19
print(grand_child.address)  # Address 15-17


# Hierarchical Inheritance- more than one child classes are created from a single parent class
class Parent2:
    def init(self, name):
        self.name = name

    def say_hi(self):
        return f"Hi! I am {self.name}"


class Daughter2(Parent2):
    def __init__(self, name):
        super().__init__(name)

    def relation(self):
        return "I am my parent's daughter"


class Son2(Parent2):
    def __init__(self, name):
        super().__init__(name)

    def relation(self):
        return "I am my parent's son"


# Method Resolution Order of a class
class Parent:
    pass
class FirstChild(Parent):
    pass
class SecondChild(Parent):
    pass
class GrandChild(SecondChild, FirstChild):
    pass
print(GrandChild.mro())  # [<class '__main__.GrandChild'>, <class '__main__.SecondChild'>, <class '__main__.FirstChild'>, <class '__main__.Parent'>, <class 'object'>]


# Mix-In - Non-complex mechanisms of multiple inheritance - only desired features from the parent class, not all of them
class Vehicle:
    def __init__(self, position):
        self.position = position
    def travel(self, destination):
        pass
class Car(Vehicle):
    pass
class Clock():
    pass
class RadioMixin():
    def play_song_on_station(self, station_frequency):
        return f'playing song on radio frequency {station_frequency}'
class Car(Vehicle, RadioMixin):
    pass
class Clock(RadioMixin):
    pass

car = Car('Sofia')
clock = Clock()
print(car.play_song_on_station(95.0))  # playing song on radio frequency 95.0
print(clock.play_song_on_station(100.3))  # playing song on radio frequency 100.3