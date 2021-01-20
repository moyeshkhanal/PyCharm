def num(i):
    if i == 0:
        return i
    print(i)
    num(i - 1)


x = 5
num(x)