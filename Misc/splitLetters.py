# # Read the file and store the State and its city, take care of duplicates
# # EX. {'OH': ['Columbus', 'Dublin', 'Westerville']}
#
# file = open("test.txt", "r")
# dictionaryY = {}
# for line in file:
#     x, y  = line.split(' ')
#     if x in dictionaryY:
#         print(dictionaryY)
#         if type(dictionaryY[x]) == list:
#             dictionaryY[x].append(y)
#         else:
#             jeff  = dictionaryY[x]
#             jeff.append(y)
#             dictionaryY[x] = jeff
#
#     else:
#         dictionaryY[x] = y
# print(dictionaryY)
# #
state = {}
with open("test.txt", "r") as file:

    for line in file:
        line = line.strip()
        x, y = line.split(" ")
        if x not in state:
            state[x] = [y]
            # print(state)
        else:
            h = state[x]
            h.append(y)
            state[x] = h

print(state)
# 
#
#
# # x, y = 4, 5
# # nums = {}
# # nums[x] = y
# # {4:5}
#
#
# import csv
# with open('csvTest.csv', 'r')as f:
#   data = csv.reader(f)
#   one = next(data)
#   print(one)