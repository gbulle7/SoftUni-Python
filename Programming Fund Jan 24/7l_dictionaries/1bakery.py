food = input().split()
bakery = {}

for index in range(0, len(food), 2):
    key = food[index]
    value = food[index + 1]
    bakery[key] = int(value)

print(bakery)

# def string_dict(elements):
#     elements = elements.split()
#     bakery = {}
#
#     for index in range(0, len(elements), 2):
#         key = elements[index]
#         value = elements[index + 1]
#         bakery[key] = int(value)
#
#     return bakery
#
#
# food = input()
# print(string_dict(food))


# class Bakery:
#     def __init__(self, elements):
#         self.elements = elements.split()
#         self.bakery = {}
#
#     def string_dict(self):
#         for index in range(0, len(self.elements), 2):
#             key = self.elements[index]
#             value = self.elements[index + 1]
#             self.bakery[key] = int(value)
#         return self.bakery
#
#
# food = input()
#
# bakery1 = Bakery(food).string_dict()
#
# print(bakery1)
