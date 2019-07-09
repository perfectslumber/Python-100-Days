x = 1
y = 1
print(x)
print(y)
for i in range(1, 101):
    z = x + y
    x = y
    y = z
    print(z)