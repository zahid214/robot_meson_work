from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    draw()
    down()
    forward()
    draw()
    down()
    forward()
    draw()
    down()
    forward()
    draw()
    down()
    
def draw():
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
        
def down():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
def forward():
    move()
    move()
    move()
    move()
if __name__ == '__main__':
    main()