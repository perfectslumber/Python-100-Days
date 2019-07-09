for x in range(1, 10000):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    if s == x:
        print(x)