# def insertionSort(nums):
# #
# #     for i in range(1, len(nums)):
# #         key = nums[i] # key = 5 Value
# #         j = i - 1 # j = 0 Index
# #         while j >= 0 and key < nums[j]:
# #             nums[j + 1] = nums[j]
# #             j = j - 1
# #         nums[j + 1] = key
# #
# #
# #
# # def main():
# #     nums = [1, 5, 3, 2, 4, 5]
# #     insertionSort(nums)
# #     print(nums)
# #
# # main()


def num(i):
    if i == 0:
        return 0
    num(i - 1)
    print(i)

num(5)
