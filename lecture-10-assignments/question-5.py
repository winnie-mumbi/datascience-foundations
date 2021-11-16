"""
Write a program that reads a grade between 1 and 5 (integer) and gives its 
description as follows:
 1:Fail, 2:Poor, 3:Fair, 4:Good, 5:Excellent

EXTRA: Now modify your program so that it prints letters for grades between 
1 and 100 using the following table 
    90–100:A, 80–89:B, 70–79:C, 60–69:D, 1–59:F

"""
def grades():
    grade = int(input("Enter number between 1 and 5: "))

    scores = {1:"Fail", 2:"Poor", 3:"Fair", 4:"Good", 5:"Excellent"}

    if grade < 1 or grade > 5:
        print("Enter number between 1 and 5")
        return
    
    score = scores[grade]

    print(score)


def grades_2():
    grade = int(input("Enter number between 1 and 100: "))
    
    if grade in range(90,101):
        print('A')
    elif grade in range(80,90):
        print('B')
    elif grade in range(70,80):
        print('C')
    elif grade in range(60,70):
        print('D')
    elif grade in range(1,60):
        print('F')
    else:
        print("Please enter a number between 1 and 100")


grades()
grades_2()