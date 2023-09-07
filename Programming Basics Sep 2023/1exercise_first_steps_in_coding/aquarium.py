length = int(input())
width = int(input())
height = int(input())
aquarium_equipment_in_percent = float(input())
percent_full = aquarium_equipment_in_percent / 100
volume_in_ltrs = length * width * height / 1000
water_needed = volume_in_ltrs * (1 - percent_full)
print(water_needed)