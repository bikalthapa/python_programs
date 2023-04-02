# python if else statement 
"""
An "if statement" is written by using the if keyword. It is used to make decision in out program
Identitation is most important for if else statement.
"""
a = 20
b = 2
if a > b:
    print("A is less than B")
elif a == b:
    print("A is equal to B")
elif a != b:
    pass  # if statements cannot be empty, but if you for some reason have an if statement with
          # no content, put in the pass statement to avoid getting an erros.
else:
    print("I don't know what is happening")


# python Short Hand conditional statement 
c = 10
d = 30
# This is short hand if statement
if c < d : print("C is less than d") 
# This is Short hand if else statement
print("C is less than D") if c < d else print("C is greater than D")