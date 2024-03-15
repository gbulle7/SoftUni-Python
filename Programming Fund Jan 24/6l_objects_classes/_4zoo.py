class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        animals = []
        if species == 'mammal':
            animals = self.mammals
            species = 'Mammals'
        elif species == 'fish':
            animals = self.fishes
            species = 'Fishes'
        elif species == 'bird':
            animals = self.birds
            species = 'Birds'
        return f"{species} in {self.zoo_name}: {', '.join(animals)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
number = int(input())

zoo = Zoo(zoo_name)

for animal_info in range(number):
    data = input().split()
    zoo.add_animal(data[0], data[1])

get_species = input()

print(zoo.get_info(get_species))
