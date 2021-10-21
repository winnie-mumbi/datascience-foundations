# A program that finds the sum of the first 1000 natural numbers

def sum():
    total = 1

    for i in range(2,1001):
        total+=i
    
    print(total)


sum()