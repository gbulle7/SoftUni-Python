money_inherited = float(input())
final_year = int(input())
age = 18
for year in range(1800, final_year + 1):
    if year % 2 == 0:
        money_inherited -= 12000
    else:
        money_inherited -= 12000 + 50 * age
    age += 1
if money_inherited >= 0:
    print(f'Yes! He will live a carefree life and will have {money_inherited:.2f} dollars left.')
else:
    print(f'He will need {abs(money_inherited):.2f} dollars to survive.')
