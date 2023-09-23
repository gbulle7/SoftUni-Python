price_bgn_vegetables_kg = float(input())
price_bgn_fruits_kg = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())
price_vegetables = price_bgn_vegetables_kg * total_kg_vegetables
price_fruits = price_bgn_fruits_kg * total_kg_fruits
total_price_eur = (price_vegetables + price_fruits) / 1.94
print(f'{total_price_eur:.2f}')
