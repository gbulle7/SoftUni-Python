v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
total_p1 = p1 * h
total_p2 = p2 * h
total_fill = total_p1 + total_p2
ratio_fill = total_fill / v * 100
ratio_p1 = total_p1 / total_fill * 100
ratio_p2 = total_p2 / total_fill * 100
if v >= total_fill:
    print(f'The pool is {ratio_fill:.2f}% full. Pipe 1: {ratio_p1:.2f}%. Pipe 2: {ratio_p2:.2f}%.')
else:
    overflow = total_fill - v
    print(f'For {h:.2f} hours the pool overflows with {overflow:.2f} liters.')
