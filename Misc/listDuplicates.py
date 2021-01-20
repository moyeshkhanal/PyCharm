nums = [1, 1, 2, 3, 3]
dups = []
for i in nums:
    if nums.count(i) > 1:
        dups.append(i)

print(dups)