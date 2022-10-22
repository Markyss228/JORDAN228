x = int(input())
y = int(input())
z = int(input())
x = x // 13
y = y // 18
z = z // 2
if z < y and z < x:
    print(z)
elif y < z and y < x:
    print(y)
elif x < z and x < y:
    print(x)