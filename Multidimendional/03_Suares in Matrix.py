rows, columns = [int(i) for i in input().split()]
matrix = [input().split() for _ in range(rows)]
# array_letters=set()
sum1 = 0
for i in range(rows - 1):
    text = "".join(matrix[i])
    test = list(zip(text, text[1:]))
    if any(s == t for s, t in zip(text, text[1:])):
        string = ''.join(str(s) for s, t in zip(text, text[1:]) if s == t)

        index1 = set([j for y in string for j in range(columns) if y == matrix[i][j]])
        text1 = "".join(matrix[i + 1])
        test = string[-1]

        result = [text1[index2:index2 + 2] == text[index2:index2 + 2] and text1[index2:index2 + 2] == string[-1] * 2 for
                  index2 in index1]
        sum1 += sum(result)

print(f'{sum1}')
