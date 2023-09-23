from math import floor, ceil

tab = '\t'

print('x \tint\tfloor\tround\tceil')
for x in (
    1.0, 1.1, 1.5, 1.9, -1.1, -1.5, -1.9,
    -2.5, -1.5, -0.5, 0.5, 1.5, 2.5,
):
    print(x, tab, int(x), tab, floor(x), tab, round(x), tab, ceil(x))
