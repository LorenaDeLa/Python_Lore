rows = int(input())
matrix = [input().split(", ") for _ in range(rows)]
diago = [i for y in matrix for i in y if y.index(i) == matrix.index(y)]
sum1 = sum(int(i) for i in diago)
print(f"primary diagonal {', '.join(diago)} Sum: {sum1}")
reverse_diag = [i for y in matrix for i in y if (y.index(i) == len(y) - matrix.index(y) - 1 and matrix.index(y) == len(y) - y.index(i)-1)]
sum1 = sum(int(i) for i in reverse_diag)
print(f"primary diagonal {', '.join(reverse_diag)} Sum: {sum1}")