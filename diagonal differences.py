#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum_diag1=0
    sum_diag2=0
    n=len(arr)
    for i in range(len(arr)):
        sum_diag1 += arr[i][i]
        sum_diag2 += arr[i][(n - 1) - i]
        diag_diff = abs(sum_diag1 - sum_diag2)
    return diag_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
