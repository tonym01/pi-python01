#!/usr/bin/env python2.7

from __future__ import print_function

def bin(x):
    return ''.join(x & (1 << i) and '1' or '0' for i in range(7,-1,-1))
# "bitwise and" operation or the inbut number when compared with 1 after shifting left by i bits  

def encoder_dir(currpins, prevpins, pinAnum, pinBnum):
    """
    calculates the direction of a rotary encoder
    returns +1, -1, or 0 (encoder not moved)
    """
    pinAmask = 1 << pinAnum
    pinBmask = 1 << pinBnum
    pinABmask = pinAmask | pinBmask
    
    if (currpins & pinABmask) != (prevpins & pinABmask): # encoder pin values have changed

        currpinA = (currpins & pinAmask) >> pinAnum
        prevpinB = (prevpins & pinBmask) >> pinBnum
        dir_ind = currpinA ^ prevpinB
        if DEBUG:
            print("DEBUG: Current pin A = ", currpinA)
            print("DEBUG: Previous pin B = ", prevpinB)
            print("DEBUG: Direction ind = ", dir_ind)

        if dir_ind == 0:
            direction = -1
        else:
            direction = 1

    else:

        direction = 0 # no change in the encoder pins, the encoder has not moved
    
    return direction
    

# this is the main logic
print("Running...\n")

pinA = 1
pinB = 0
position = 0 # initial position of the encoder
DEBUG = True
prevnum = 0b00000010 # 

try:
    while(True):
        print("Input value for encoder pins. Prev value= ", prevnum, "\n")
        input = raw_input("> ")
        num = int(input)
        d = encoder_dir(currpins=num, prevpins=prevnum, pinAnum=pinA, pinBnum=pinB)
        print("calculated direction = ", d)
        if d != 0:
            prevnum = num
            position += d
            print("Position now = ", position)
          
except KeyboardInterrupt:
    print("\nInterrupted...")

print("Bye!")
