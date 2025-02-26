# Exercise 3:
# Write Python code which starts with the number 1 and then displays
# the result of halving the previous number until the result is less than 0.001.
# The expected output should be: 1.0 0.5 0.25 0.125 0.0625 0.03125 0.015625 0.0078125 0.00390625 0.001953125
i=1
while i>0.001:
    print(i, end=' ')
    i=i/2
