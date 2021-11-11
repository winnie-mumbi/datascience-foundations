"""
if you replace the statement fact = fact * factor with fact = fact * 5, 
what would this function compute? Run the modified program and try with different values.

answer:
the function will multiply '5' with itself 'n' number of times

"""
def main():
    n = int(input("Enter a number"))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * 5
    
    print("The ans is ",fact)

main()
