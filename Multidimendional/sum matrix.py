rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)


sume = sum([i for y in matrix for i in y])
print(f'{sume} \n {matrix}')