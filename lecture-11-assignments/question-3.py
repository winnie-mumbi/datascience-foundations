def sumnum(num1, num2, k):
    total = 0
    for num in range(num1,num2+1):
        total+=num**k
    return total

def mainsum():
    a = 50
    b = 150
    k = 2
    print("Sum of %d power of numbers from %d to %d = %d" % (k, a, b, sumnum(a, b, k)))


mainsum()