"""
In the following program, what is the value of x after the loop finishes (final value)?
What would be the final value of x for the cases where the initial value of x is 6, 5, and 8? 


When initial value of x is:
    x = 7 ; infinite loop
    x = 6 ; infinite loop
    x = 5 ; final_value_of_x = 4 
    x = 8 ; final_value_of_x = 9
"""

def final_val2():
    x = 7

    while x >=5 and x <=8:
        print(x)
        if x % 2 == 0:
            x = x + 1
        else:
            x = x - 1
    

    print(f"Final value", x)

final_val2()