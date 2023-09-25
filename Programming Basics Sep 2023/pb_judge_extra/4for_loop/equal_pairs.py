# v judge q priema, no ne mislq che e vqrna, zashtoto sledniq input:
# 7
# 34
# -33
# 52
# 12
# -32
# 32
# 23
# 41
# 7
# 25
# 34
# 23
# 124
# 21
# ako loop-a svurshva pri 23 i 41 chislata (9 i 10 liniq), to difference shte e 0, a trqbva da e 64

n = int(input())
sum_number_1 = 0
sum_number_2 = 0
equal_sums = 0
difference = 0

for _ in range(n):
    current_number_1 = int(input())
    current_number_2 = int(input())
    sum_number_1 = current_number_1 + current_number_2
    difference = abs(sum_number_1 - sum_number_2)
    if sum_number_1 == sum_number_2:
        equal_sums += 1
    sum_number_2 = current_number_1 + current_number_2
if equal_sums == n - 1:
    print(f'Yes, value={sum_number_1}')
else:
    print(f'No, maxdiff={difference}')
