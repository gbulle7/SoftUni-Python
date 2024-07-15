# # static methods
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
#
# print(Person.is_adult(5))  # False
# girl = Person("Amy")
# print(girl.is_adult(20))  # True
#
#
# # class methods
# class Pizza:
#      def __init__(self, ingredients):
#         self.ingredients = ingredients
#      @classmethod
#      def pepperoni(cls):
#         return cls(["tomato sauce", "parmesan", "pepperoni"])
#      @classmethod
#      def quattro_formaggi(cls):
#         return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])
# first_pizza = Pizza.pepperoni()
# second_pizza = Pizza.quattro_formaggi()



# Overriding using methods
# class Person:
#      min_age = 0
#      max_age = 150
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
#      @staticmethod
#      def __validate_age(value):
#         if value < Person.min_age or value > Person.max_age:
#             raise ValueError()
#      @property
#      def age(self):
#         return self.__age
#      @age.setter
#      def age(self, value):
#         self.__validate_age(value)
#         self.__age = value
#
# class Employee(Person):
#      min_age = 16
#      max_age = 150
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
#
#     @staticmethod
#     def __validate_age(value):
#          if value < Employee.min_age or value > Employee.max_age:
#             raise ValueError()
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, value):
#         self.__validate_age(value)
#         self.__age = value


class Person:
    min_age = 0
    max_age = 150
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def __validate_age(cls, value):
        raise ValueError(f'{value} must be between '
                         f'{cls.min_age} and {cls.max_age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):
    min_age = 16

    # __validate_age() takes the class attribute min_age of class Employee
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # when checking the age of the Employee
        self.salary = salary
