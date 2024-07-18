class Shape:
    def calculate_area(self):
        return None


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


for obj in Square(), Triangle():
    if isinstance(obj, Square):
        area = obj.calculate_square_area()
    elif isinstance(obj, Triangle):
        area = obj.calculate_triangle_area()
    print(area)


# Overloading __add__()
class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost
    def __add__(self, other):
        name = f'{self.product_name}, {other.product_name}'
        cost = self.cost + other.cost
        return Purchase(name, cost)
first_purchase = Purchase('sofa', 650)
second_purchase = Purchase('table', 150)
print(first_purchase + second_purchase)  # sofa, table; 800


# Overloading __gt__()
class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __gt__(self, other):
        return self.salary > other.salary
person_one = Person('John', 20)
person_two = Person('Natasha', 36)
print(person_one > person_two)  # False


# Duck Typing
class Cat:
    def sound(self):
        print("Meow!")
class Train:
    def sound(self):
        print("Sound from wheels slipping!")
for any_type in Cat(), Train():
    any_type.sound()


# Abstract class using exception /bad practice/
# class Shape:
#     def __init__(self):
#         if type(self) is Shape:
#             raise Exception('This is an abstract class')
#     def area(self):
#         raise Exception('This is an abstract class')
#     def perimeter(self):
#         raise Exception('This is an abstract class')


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        raise NotImplementedError("Subclass must implement")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Bark!")
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Meow!")
cat = Cat("Willy")
cat.sound()  # Meow!
dog = Dog("Willy")
dog.sound()  # Bark!
animal = Animal("Willy")
animal.sound()  # Error!
