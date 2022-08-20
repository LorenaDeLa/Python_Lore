count = int(input())
students = {}
for _ in range(count):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))
for key, value in students.items():
    average = sum(value) / float(len(value))
    test = str.join("", str(value))

    print(f"{key} {test} (average {average})")


