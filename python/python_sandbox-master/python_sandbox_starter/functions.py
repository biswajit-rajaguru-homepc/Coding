# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def factorial(n):
    if n == 1:
        return 1
    else :
        return n * factorial(n-1)

#print( factorial(500))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

mysum = lambda n1, n2 : n1+n2

print(mysum(1,2))
