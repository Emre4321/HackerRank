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
    answer = []
    for hashtags in range(1, n + 1):
        answer.append(" " * (n - hashtags) + "#" * hashtags)
        print(answer[hashtags - 1])

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
