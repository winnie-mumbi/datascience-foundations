# A program that finds the factorial of a user's input

def factorial():
    n = int(input("Enter a number"))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    
    print("The factorial of",n,"is",fact)


factorial()