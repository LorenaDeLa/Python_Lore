def negatives(*args):
    # lis= list(args)

    sum1 = sum(i for i in args if i > 0)
    sum2 = sum(i for i in args if i < 0)
    print(f'{sum1}\n{sum2}')
    if abs(sum1) > abs(sum2):
        print(f"The positives are stronger than the negatives")
    else:
        print('The negatives are stronger than the positives')


numb = [(int(i)) for i in input().split()]
numb = tuple(numb)
negatives(*numb)




