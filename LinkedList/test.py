# lst = [x for x in range(100)]
#
div = 0

for i in range(1,10):
    for x in range(100):
        if x % i == 0:
            div += 1
    print(f"There are {div} numbers that can be divided by {i}")
    div = 0

x = 1

for i in range(9):
    print("The numbers that are divisible by ", x, " are: ")
    for y in range(100):
        z = y / x
        if y == 0:
            print("Num is 0")
            pass
        elif z.is_integer():
            # print(y)
            pass
        else:
            pass
    if x == 10:
        break
    x += 1
