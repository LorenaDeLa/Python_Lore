rows, cols = [int(i) for i in input().split(", ")]

matrix = []

for i in range(rows):
    row = input().split(", ")
    matrix.append(list(map(int, row)))
evens = [[x for x in row if x % 2 == 0] for row in matrix]

print(evens)

