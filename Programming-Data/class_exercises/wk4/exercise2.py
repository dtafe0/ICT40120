# Exercise 2:
# Write Python code which displays the numbers 12 to 1 separated by commas “,”.
# Make sure the last number is not displaying the comma after it.
# The expected output should be: 12,11,10,9,8,7,6,5,4,3,2,1

i=12
while i>1:
    print(i, end=',')
    i -= 1
print(1)
