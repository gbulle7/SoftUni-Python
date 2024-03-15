class Party:
    people = []


name = input()
while name != 'End':
    Party().people.append(name)
    name = input()

print(f"Going: {', '.join(Party().people)}")
print(f'Total: {len(Party().people)}')


# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
#
# while True:
#     name = input()
#     if name == 'End':
#         break
#     party.people.append(name)
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")


# class Party:
#     def __init__(self):
#         self.people = []
#
#     def add_person(self, name):
#         self.people.append(name)
#
#     def get_party_info(self):
#         return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"
#
#
# party = Party()
#
# while True:
#     name = input()
#     if name == 'End':
#         break
#     party.add_person(name)
#
# print(party.get_party_info())