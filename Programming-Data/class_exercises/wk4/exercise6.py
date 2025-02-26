# Exercise 6:
# Repeat your code from the previous task inside a new .py file.
# In addition to the lowest number, display the highest and the average of the 10 numbers.

import random

numbers = []
for k in range(10):
    rand_num = random.randint(0, 50)
    numbers.append(rand_num)
    print(rand_num, end=' ')

lowest = min(numbers)
highest = max(numbers)

print('The lowest number is: ', lowest)
print('The highest number is: ', highest)