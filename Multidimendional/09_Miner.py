rows = int(input())
command = input().split()
matrix = [input().split() for _ in range(rows)]
start = [(i, y.index("s")) for i, y in enumerate(matrix) if "s" in y]
numbers = len([(i, j) for i, y in enumerate(matrix) for j in y if "c" in j])
x, y = start[0]

for _ in range(len(command) ):
    order = command.pop(0)

    if order == "up":
        x -= 1
    elif order == "right":
        y += 1
    elif order == "left":
        y -= 1
    elif order == "down":
        x += 1
    if x > rows - 1: x = rows - 1
    if y > rows - 1: y = rows - 1
    if x < 0: x = 0
    if y < 0: y = 0
    tupe = (x,y)
    if "e" in matrix[x][y]:
        print(f"game over! {tupe}")
        break
    elif "c" in  matrix[x][y]:
        matrix[x][y]= "*"
        numbers -=1



if numbers == 0:
    print(f'You collected all coal {tupe}')
else:
    print(f'{numbers} pieces remaining of coal {tupe}')
