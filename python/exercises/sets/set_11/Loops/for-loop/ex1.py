# ForLoop :
# Python for loop is used for repeated execution of a group of statements for thr desired number of times
# It iterates over the items of list,truples,strings,dictionaries.

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [15,5,10,20,30,25]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)