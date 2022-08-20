number = int(input())
even = set()
odd = set()
for i in range(number):
    name = input()
    sume1 = int(sum(ord(y) for y in name) / (i + 1))
    if sume1 % 2 == 0:
        even.add(sume1)
    else:
        odd.add(sume1)

sum1 = (sum(i for i in even))
sum2 = (sum(i for i in odd))

if sum1 == sum2:
    text = ', '.join(map(str, even | odd))

elif sum2> sum1:
    text = ', '.join(map(str, odd - even))
else:
    text = ','.join(map(str, even ^ odd))


print(f'{text}') 