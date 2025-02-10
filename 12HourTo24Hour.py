#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    #Expected format is HH:MM:SS(AM/PM) (No spaces)
    AMorPM = s[-2:]
    hour = s[0] + s[1]
    minute = s[3] + s[4]
    second = s[6] + s[7]
    if int(hour) == 12 and AMorPM == "AM":
        hour = "00"
    elif AMorPM == "PM" and hour != "12":
        hour = str(int(hour) + 12)
    answer = str(hour) + ":" + minute + ":" + second
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
