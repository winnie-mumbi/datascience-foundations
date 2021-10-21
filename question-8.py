#  A program that finds the average of 5 numbers entered by user

def average():
    total = 0

    for i in range(5):
        num = float(input("Enter a number:"))
        total+=num
    
    average = total/5
    print(average)


average()