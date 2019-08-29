#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    add=0
    for i in range(len(ar)):
        add+= ar[i]
    return add
    
# main function to call it
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()