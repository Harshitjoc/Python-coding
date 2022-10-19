#hacker rank problem solving question
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):

    x = ""
    y = "#"
    for i in range(n):
        x = y * (i+1)
        print(x.rjust(n))
   
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
