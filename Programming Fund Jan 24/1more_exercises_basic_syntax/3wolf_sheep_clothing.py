animal_type = input()

my_list = animal_type.split(', ')

for index, animal in enumerate(reversed(my_list)):
    if animal == 'wolf':
        if index == 0:
            print(f'Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
            break

# animals = input().split(", ")
# wolf_index = animals.index('wolf') + 1
# sheep_index = len(animals) - wolf_index
# if wolf_index == len(animals):
#     print("Please go away and stop eating my sheep")
# else:
#     print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")

# animals = input()
# animals_list = animals.split(', ')
# animals_list.reverse()
# for index, animal in enumerate(animals_list):
#     if animal == 'wolf' and index == 0:
#         print('Please go away and stop eating my sheep')
#     elif animal == 'wolf':
#         print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')