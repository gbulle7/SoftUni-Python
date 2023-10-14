command = input()
adults = 0
kids = 0
toys = 0
sweaters = 0

while command != 'Christmas':
    age = int(command)
    if age <= 16:
        toys += 1
        kids += 1
    else:
        sweaters += 1
        adults += 1
    command = input()

sweaters_price = sweaters * 15
toys_price = toys * 5

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys_price}")
print(f"Money for sweaters: {sweaters_price}")
