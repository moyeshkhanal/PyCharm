
# First line is N integer
# Y = mx + b

# Second lines m, x, b

with open("line.txt") as file:
    # read the first line
    n = file.readline()

    for i in range(int(n)):
        line = file.readline().strip()
        m, x, b = line.split(" ")
        m = int(m)
        x = int(x)
        b = int(b)
        print(m * x + b)