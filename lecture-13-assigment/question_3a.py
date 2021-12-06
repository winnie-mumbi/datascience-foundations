"""
In the following program, what is the value of i after the loop finishes (final value)?
What would be the final value of i for the cases where you decrement i by 2, 4, 5, and 10 (instead of 3)?

Final value of i when decremented by:
    3 is 10
    2 is 11
    4 is 9
    5 is 10
    10 is 5
"""

def final_val():
    i = 25

    while i > 12:
       print(i)
       i = i - 3
    
    print(f"Final value:" ,i)


final_val()