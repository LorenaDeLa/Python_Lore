Test=input()
array= set()
for i in Test:
    array.add(i)

s=sorted(list(array))
for letter in s:

    print(f' {letter} : {Test.count(letter)} times/s')