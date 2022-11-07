#hacker rank problem solving question

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive_count+=1
        elif i < 0:
            negative_count+=1
        else:
            zero += 1
    print(positive_count/len(arr))
    print(negative_count/len(arr))
    print(zero/len(arr))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
