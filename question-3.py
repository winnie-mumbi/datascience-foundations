# A program that gets square root of a user's input

import cmath
# imported cmath instead to handle negative numbers

def main():
    num = int(input("Enter a number:"))
    result = cmath.sqrt(num)

    print("The square of",num,"is",result)


main()