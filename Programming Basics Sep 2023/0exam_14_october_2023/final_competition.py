dancers = int(input())
points = float(input())
season = input()
location = input()
prize = 0

if location == 'Bulgaria':
    prize = points * dancers
    if season == 'summer':
        prize *= 0.95
    elif season == 'winter':
        prize *= 0.92
elif location == 'Abroad':
    prize = (dancers * points) * 1.5
    if season == 'summer':
        prize *= 0.90
    elif season == 'winter':
        prize *= 0.85

charity_sum = prize * 0.75
remaining_money = prize - charity_sum
money_per_dancer = remaining_money / dancers

print(f"Charity - {charity_sum:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
