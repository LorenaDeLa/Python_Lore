num=int(input())
s=set()
for i in range(num):
    string= input().replace("-",",")
    first_start, first_end,second_start, second_end= string.split(",")

    s1 = {i for i in range(int(first_start),int(first_end)+1)}
    s2 = {i for i in range(int(second_start),int(second_end)+1)}
    s3 = s1 & s2
    if len(s)< len(s3):
        s = s3


print(f"{s} with length {len(s)}")