# Function to do insertion sort
def insertionSort(num):
    # Traverse through 1 to len(arr)
    for i in range(1, len(num)):

        key = num[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < num[j]:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key


def main():
    num = [1, 5, 3, 2, 4]
    insertionSort(num)

    print(num)

main()