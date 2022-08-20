rows, columns = [int(i) for i in input().split()]

matrix= [str(chr(97 + i)+ chr(97 + i+ j)+ chr(97 + i)) for i in range(rows) for j in range(columns)]


matrix1= [matrix[i:i + columns ] for i in range(0,len(matrix),columns)]
for i in matrix1:
    print(f'{" ".join(i)}')