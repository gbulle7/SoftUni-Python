rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for i in range(rows)]

primary_diag = [matrix[i][i] for i in range(rows)]
secondary_diag = [matrix[i][rows - 1 - i] for i in range(rows)]     # matrix[i][-i-1]
print(f'Primary diagonal: {", ".join(map(str, primary_diag))}. Sum: {sum(primary_diag)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diag))}. Sum: {sum(secondary_diag)}')
