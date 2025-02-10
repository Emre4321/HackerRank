#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sortedarray = sorted(arr)
    firstvalue = sortedarray[0] + sortedarray[1] + sortedarray[2] + sortedarray[3]
    secondvalue = sortedarray[1] + sortedarray[2] + sortedarray[3] + sortedarray[4]
    print(firstvalue, secondvalue)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
