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
    hashtags = 1
    answer = []
    for number in range(n):
        answer.append(" " * (n - hashtags) + "#" * hashtags)
        print(answer[hashtags - 1])
        hashtags += 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
