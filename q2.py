t1 = 1
t2 = 2
c = 2

while t1<10**6:
    t1 = t1+t2
    t2 = t1+t2

    if t1 % 2 == 0:
        c += t1

    if t2 % 2 == 0:
        c += t2

print(c)