"""
Write a program that reads a grade between 1 and 5 (integer) and gives its 
description as follows:
 1:Fail, 2:Poor, 3:Fair, 4:Good, 5:Excellent

EXTRA: Now modify your program so that it prints letters for grades between 
1 and 100 using the following table 
    90–100:A, 80–89:B, 70–79:C, 60–69:D, 1–59:F

"""
def grades():
    grade = int(input("Enter a number between 1 and 5: "))

    grading = {1: "Fair", 2:"Poor",3:"Fair",4:"Good",5:"Excellent"}

    if grade in range(1,6):
        desc = grading[grade]
        print(f"Your grade is {desc}")
    else:
        print("Invalid grade.Enter a number from 1 to 5")

def grades_2():
    score = int(input("Enter a number between 1 and 100: "))

    if score >= 1 and score < 101:
        if score in range(90,101):
            print('A')
        elif score in range(80,90):
            print('B')
        elif score in range(70,80):
            print('C')
        elif score in range(60,70):
            print('D')
        else:
            print('F')
    else:
        print("Invalid grade.Enter a number from 1 to 100")

grades()
grades_2()