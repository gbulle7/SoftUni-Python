from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def food_edible(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def food_edible(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def food_edible(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.30


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def food_edible(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1
