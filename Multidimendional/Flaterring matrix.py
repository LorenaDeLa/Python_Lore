rows_count, cols = [int(i) for i in input().split(", ")]
matrix = [map(int, input().split(', ')) for _ in range(rows_count)]
flattened = [num for row in matrix for num in row]
print(flattened)
