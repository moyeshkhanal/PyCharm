import time

def diff():
    str = "hello"

    left = ""
    right = ""
    duplicates = {}
    s = time.time()
    for i in str:
        time.sleep(0)
        if "a" <= i <= "m":
            if i in duplicates:
                left += i
            else:
                duplicates[i] = 0
        elif "n" <= i <= "z":
            if not(i in duplicates):
                right += i
            else:
                duplicates[i] = 0
    e = time.time()
    print(left + "|" + right)
    print(e-s)



def main():
    str = "hello"

    left = ""
    right = ""
    s = time.time()
    for i in str:
        count = 0
        time.sleep(0)
        if "a" <= i <= "m":
            for x in left:
                if i == x:
                    count += 1
            if count < 1:
                left += i
        elif "n" <= i <= "z":
            for x in right:
                if i == x:
                    count += 1
            if count < 1:
                right += i
    e = time.time()
    print(left + "|" + right)
    print(e-s)

main()