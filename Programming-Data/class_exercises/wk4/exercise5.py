# Exercise 5:
# Repeat your code from the previous task inside a new .py.
# In addition to generating the 10 random numbers, display the lowest of the 10 numbers.

import random
numbers = []
for k in range(10):
    rand_num= random.randint(0,50)
    numbers.append(rand_num)
    print(rand_num, end=' ')
    
lowest =min(numbers)
print('The lowest number is: ', lowest)
