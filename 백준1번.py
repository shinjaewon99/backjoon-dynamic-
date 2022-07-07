a= int(input())

def sum(a):
    if a ==1:
        return 1
    if a == 2:
        return 2
    if a == 3:
        return 4
    else :
        return sum(a-1) + sum(a-2) + sum(a-3)

for i in range(a):
    n = int(input())

    print(sum(n))


