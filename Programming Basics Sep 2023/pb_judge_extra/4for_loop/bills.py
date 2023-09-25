period_months = int(input())
water_bill = 20
internet_bill = 15
water_bill_total = water_bill * period_months
internet_bill_total = internet_bill * period_months
electricity_bill_total = 0
others_bill_total = 0

for _ in range(period_months):
    electricity_bill = float(input())
    electricity_bill_total += electricity_bill
    others_bill = (water_bill + internet_bill + electricity_bill) * 1.2
    others_bill_total += others_bill
total_bills = water_bill_total + internet_bill_total + electricity_bill_total + others_bill_total
average_bills = total_bills / period_months

print(f'Electricity: {electricity_bill_total:.2f} lv')
print(f'Water: {water_bill_total:.2f} lv')
print(f'Internet: {internet_bill_total:.2f} lv')
print(f'Other: {others_bill_total:.2f} lv')
print(f'Average: {average_bills:.2f} lv')
