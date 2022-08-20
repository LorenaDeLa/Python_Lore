def age_assignment(*args, **kwargs):
    dit = dict()
    for i in args:
        dit[i] = kwargs[i[0]]

    return dit


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
