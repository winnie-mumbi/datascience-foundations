"""
If you continually divide a number by 2, it will equal to zero after you do the division infinite number of times:
The sequence 1, ½, ¼, 1/8, 1/16, ... 1/2n approaches 0 as n approaches infinity.
However, when you use a float, because of the rounding errors, the result becomes zero after a number of steps (before infinity).
Let’s see this using a while loop.

In the beginning of the program, initialize a float variable to 1 (e.g. x=1.0 ).
Then, in a while loop, continually divide x by 2 (x=x/2).
When the loop finishes, the program should print an appropriate message.
Do you think this loop will stop or will it run forever? 
    - depends on the loop condtion
    - if the condition does not check whether the num is 0,it will run forever
"""

def division():
    num = 1.0

    while num != 0:
        num = num / 2

division()