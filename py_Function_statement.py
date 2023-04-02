"""
Python Fucntion--------
A function is the block of statement that performs certain tasks by taking input as parameter.
"""

# declaration of functions
def add(a,b) :  # if we have limited arguments then we can get argument like this
        sum = a + b
        print("The Sum of given number is " + str(sum))
def sub(*numbers) : # if we have unlimited arguments then we can get argument like this..
        difference = numbers[0] - numbers[1]
        print("The difference is " + str(difference))
# Calling a functions by passing arguments.
sub(20,5)
add(1,2)