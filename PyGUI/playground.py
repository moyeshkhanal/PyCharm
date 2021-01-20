word = ["Hi", "World", "Apple", "Banana"]

for i in range(len(word)):
    print(i, word[i])

print("enum")
for i, w in enumerate(word):
    print(i, w)