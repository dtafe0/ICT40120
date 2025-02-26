# Exercise 4:
# Write Python code which generates and displays 10 random (integer) numbers between 0 and 50.
# Note that each time this program runs the results are different.
import random

for _ in range(10):
    i = random.randint(0,50)
    print(i, end=' ')
