# protected
# class Person:
#     def __init__(self, name, age=0):
#         self.name = name
#         self._age = age
#
#
# person = Person('Peter', 25)
# print(person.name)  # Peter
# print(person._age)  # 25


# private
# class Person:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.__age = age
#     def info(self):
#         print(f"I am {self.name}, {self.__age} years old.")
# person = Person('Peter', 25)
# # accessing data using the class method
# person.info() # I am Peter, 25 years old.
# # accessing data directly from outside
# print(person.name)  # Peter
# print(person.__age)  # AttributeError: 'Person' object has no attribute '__age'


# name mangling
# class Car:
#     def __init__(self):
#         self.__max_speed = 200
#
#     def drive(self):
#         print('driving max speed ' + str(self.__max_speed))
# red_car = Car()
# red_car.drive()  # driving max speed 200
# red_car.__max_speed = 10  # won't change because it is name mangled
# red_car.drive()  # driving max speed 200


# getter and setter methods
# class Person:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.__age = age
#     def info(self):
#         print(self.name)
#         print(self.__age)
#     def get_age(self):  # getter
#         print(self.__age)
#     def set_age(self, age):  # setter
#         self.__age = age
# person = Person('Peter', 25)
# # accessing data using class method
# person.info()  # Peter # 25
# # changing age using setter
# person.set_age(26)
# person.get_age()  # 26


# using properties
# class Person:
#     def __init__(self, age=0):
#         self.age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if age < 18:
#             self.__age = 18
#         else:
#             self.__age = age
# person = Person(25)
# print(person.age) # 25
# person.age = 10
# print(person.age) # 18


# class Car:
#     def __init__(self, max_speed: int):
#         self.max_speed = max_speed
#     def drive(self):
#         print('driving max speed ' + str(self.max_speed))
#     @property
#     def max_speed(self):
#         return self.__max_speed
#     @max_speed.setter
#     def max_speed(self, value):
#         if value > 447:
#             value = 447
#         self.__max_speed = value
# red_car = Car(200)
# red_car.drive() # driving max speed 200
# red_car.max_speed = 512 # changes the speed to 447
# red_car.drive() # driving max speed 447


# apply rules to an attribute
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, value):
#         if value <= 0:
#             raise Exception("Age must be greater than zero")
#         self.__age = value


# name mangling a method
# class Person:
#     def __init__(self):
#         self.first_name = 'Peter'
#         self.last_name = 'Parker'
#     def __full_name(self):
#         return f'{self.first_name} {self.last_name}'
#     def info(self):
#         return self.__full_name()


# getattr()
# class Person:
#     def __init__(self, name):
#         self.name = name
# person = Person('Peter')
# print(getattr(person, 'name'))  # Peter
# print(getattr(person, 'age'))  # AttributeError
# print(getattr(person, 'age', 'None'))  # None


# accessing phone.color, Python calls phone.__getattr__('color')
# class Phone:
#     def __getattr__(self, attr):
#         return None
# phone = Phone()
# print(phone.color) # None
# print(getattr(phone, 'size')) # None


# hasattr()
# class Person:
#     def __init__(self, name):
#         self.name = name
# person = Person('Peter')
# print(hasattr(person, 'name'))  # True
# print(hasattr(person, 'age'))  # False


# setattr()
# class Person:
#     def __init__(self, name):
#         self.name = name
# person = Person('Peter')
# print(setattr(person, 'name', 'George'))  # None
# print(person.name)  # George
# print(setattr(person, 'age', 21))  # None
# print(person.age)  # 21


# attribute assignment using __setattr__
# class Phone:
#     def __setattr__(self, attr, value):
#         self.__dict__[attr] = value.upper()
# phone = Phone()
# phone.color = 'black'
# print(phone.color)  # BLACK


# delattr()
# class Person:
#     def __init__(self, name):
#         self.name = name
# person = Person('Peter')
# print(person.name)  # Peter
# print(delattr(person, 'name'))  # None
# print(person.name)  # AttributeError


# attribute deletion using __delattr__
# class Phone:
#     def __delattr__(self, attr):
#         del self.__dict__[attr]
#         print(f"'{str(attr)}' was deleted")
# phone = Phone()
# phone.color = 'black'
# del phone.color  # 'color' was deleted


class Employee:
    name = 'Nomis'
    salary = '25000'
    def show(self):
        print(self.name)
        print(self.salary)
employee = Employee()
print(getattr(employee, 'name')) # Nomis
print(hasattr(employee, 'name')) # True
setattr(employee, 'height', 182)
print(getattr(employee, 'height')) # 182
delattr(Employee, 'salary')
