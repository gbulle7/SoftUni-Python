rows = int(input())
matrix = [[int(x) for x in input().split()] for i in range(rows)]

primary_diag = [matrix[i][i] for i in range(rows)]
secondary_diag = [matrix[i][rows - 1 - i] for i in range(rows)]

print(abs(sum(primary_diag) - sum(secondary_diag)))
