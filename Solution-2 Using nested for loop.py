Solution-2: Using nested for loop


import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
t = []
for i in range(n):
    matrix_item = [x for x in input()]
    matrix.append(matrix_item)
    
for i in range(m):
    for j in range(n):
        t.append(matrix[j][i])

s = ''.join(t)

path = re.compile(r'\b[ !@#$%&]+\b', re.M)
k = re.sub(path, ' ', s)
print(k)