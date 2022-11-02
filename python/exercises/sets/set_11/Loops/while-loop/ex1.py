# While Loop :
# while loop provides to repeat one or more statements while a particular condition is True.
# While loop, the condition is tested before any of the statements in the statement block is executed
# If the condition is True, only then the statements will be executed 
# otherwise if the condition is False, it is jump to next statement which is outside of the while loop.
# Note: If the condition of a while loop is never updated and condition never become False, 
# then the computer will run into an infinite loop.

# Program to add natural
# numbers up to 
# sum = 1+2+3+...10

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)