budget = float(input())
gpu_number = int(input())
cpu_number = int(input())
ram_number = int(input())
total_gpu_price = gpu_number * 250
cpu_price = total_gpu_price * 0.35
ram_price = total_gpu_price * 0.1
total_cpu_price = cpu_number * cpu_price
total_ram_price = ram_number * ram_price
total_price = total_gpu_price + total_cpu_price + total_ram_price
if gpu_number > cpu_number:
    total_price *= 0.85  # 15% discount
difference = abs(total_price - budget)
if budget >= total_price:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')

