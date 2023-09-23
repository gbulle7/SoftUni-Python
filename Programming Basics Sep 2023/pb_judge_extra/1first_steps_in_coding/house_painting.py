house_height = float(input())
side_wall_length = float(input())
height_triangle_roofwall = float(input())
door_area = 1.2 * 2
window_area = 1.5 * 1.5
front_wall_area = house_height * house_height - door_area
back_wall_area = house_height * house_height
side_wall_area = side_wall_length * house_height - window_area
total_green_area = front_wall_area + back_wall_area + 2 * side_wall_area
green_paint_liters = total_green_area / 3.4
roof_rectangle_area = house_height * side_wall_length
roof_triangle_area = house_height * height_triangle_roofwall / 2
total_red_area = roof_rectangle_area * 2 + roof_triangle_area * 2
red_paint_liters = total_red_area / 4.3
print(f'{green_paint_liters:.2f}')
print(f'{red_paint_liters:.2f}')
