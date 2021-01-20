
name = "Mo"
print("My name is {} {}".format(name, 20))

# Python 3.6
print(f'My name is {name}, I am {20} years old')

val = 12.65465
print(f'{val:.3f}')
print(f'{val:.5f}')

import math
x = 0.8
print(f'{math.cos(x) = }')
print(f'{math.sin(x) = }')
print(f'{x = }')

# Width for the numbers
for x in range(1, 11):
    print(f'{x**2:0>3} {x*x:0>4} {x*x*x:0>5}')

import datetime
now = datetime.date(2020,11,18)
# print(type(now))
print(f'{now:%A %b %c}')

# String Formatting
s1 = 5
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')