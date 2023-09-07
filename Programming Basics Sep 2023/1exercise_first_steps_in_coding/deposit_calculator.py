deposit = float(input())
time = float(input())
annual_inflation_rate = float(input())
rate_in_decimal = annual_inflation_rate / 100
total_sum = deposit + time * ((deposit * rate_in_decimal) / 12)
(print(total_sum))