from collections import deque

queue = deque()

while True:
    command = input()
    if command == "Paid":
        while len(queue):
            print(queue.popleft())
    elif command == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)

while command != "End":
    if command == "Paid":
        while len(queue):
            print(queue.popleft())
    else:
        queue.append(command)

else:
    print(f"{len(queue)} people remaining.")
