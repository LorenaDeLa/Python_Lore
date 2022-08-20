from collections import deque

queue = deque()
quantity = int(input())
name = input()
liter_l = quantity
while name != "Start":
    queue.append(name)
    name = input()

while name != "End":

    if name.isdigit():
        if (liter_l - int(name)) >= 0:
            print(f'{queue.popleft()} got water')
            liter_l -= int(name)
        else:
            print(f'{queue.popleft()} must wait')
    elif "refill" in name:
        re, name = name.split()
        liter_l += int(name)

    name = input()

else:
    print(f'{liter_l} liters left')
