from math import ceil

paint_number = int(input())
wallpapers_number = int(input())
gloves_pair_price = float(input())
brush_price = float(input())

paint_price = paint_number * 21.5
wallpaper_price = wallpapers_number * 5.2
gloves_pair_number = ceil(wallpapers_number * 0.35)
gloves_price = gloves_pair_price * gloves_pair_number
brush_number = int(paint_number * 0.48)
total_brush_price = brush_price * brush_number
total_price = total_brush_price + paint_price + wallpaper_price + gloves_price
delivery_price = total_price / 15

print(f"This delivery will cost {delivery_price:.2f} lv.")
