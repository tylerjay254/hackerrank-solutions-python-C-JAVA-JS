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
    # code 
    negarr = []
    posarr = []
    zeroarr = []
    for i in arr:
        if i < 0:
            negarr.append(i)
        elif i > 0:
            posarr.append(i)
        else:
            zeroarr.append(i)
        
    posratio = float("{:0.6f}".format(len(posarr) / len(arr)))
    negratio = float("{:0.6f}".format(len(negarr) / len(arr)))
    zeroratio= float("{:0.6f}".format(len(zeroarr) / len(arr)))
    
    print (posratio)
    print (negratio)
    print (zeroratio)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
