# people_number = int(input())
# capacity_people = int(input())
#
# rounds = people_number // capacity_people
# remainder = people_number % capacity_people
#
# if remainder > 0:
#     rounds += 1
#
# print(rounds)

people_number = int(input())
capacity_people = int(input())

from math import ceil
rounds = ceil(people_number / capacity_people)

print(rounds)

