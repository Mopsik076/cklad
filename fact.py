n = int(input('Число:'))

def fact(a):
    if a == 1:
        return 1
    else:
        return a*fact(a-1)

print(fact(n))
