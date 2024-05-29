def fill_the_box(*args):    # fill_the_box(height, length, width, *args)
    height, length, width, *cubes = args
    box_volume = height * length * width
    filled_space = 0
    for cube in cubes:
        if cube == 'Finish':
            break
        filled_space += cube

    if filled_space < box_volume:
        return f'There is free space in the box. You could put {box_volume - filled_space} more cubes.'
    else:
        return f'No more free space! You have {filled_space - box_volume} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
