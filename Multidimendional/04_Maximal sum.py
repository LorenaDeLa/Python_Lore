rows, columns = [int(i) for i in input().split()]
matrix=[input().split() for _ in range(rows)]
sum1=0
master=[]
for i in range (rows - 2):
    for k in range(columns-2):
        test = [matrix[x+i][k:k+3] for x in range(3)]
        sum2= sum(int(o) for u in test for o in u)

        # matrix1= [j for y in matrix[i:3] for j in y[0:3]]
        # sum2 = sum(int(j) for y in matrix[i:3] for j in y[0:3])
        if sum1<sum2:
            sum1=sum2
            master=test

print(f'{sum1}')
print(f"{master}")