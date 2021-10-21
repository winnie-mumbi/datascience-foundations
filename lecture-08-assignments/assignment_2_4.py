# A program that computes a given integer power of a given number
def main():
    base = int(input("Enter a base number:"))
    exponent= int(input("Enter an exponent number:"))

    result = base
    for i in range(exponent-1):
        result = result * base
        
    print(base,"to the power of",exponent,"is",result)


main()