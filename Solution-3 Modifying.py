Solution-3: Modifying previous solution

import re

# Read n and m from the input
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

# Read the matrix script from the input
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Decode the matrix script
decoded_script = ""
for j in range(m):
    for i in range(n):
        decoded_script += matrix[i][j]

# Replace symbols or spaces between two alphanumeric characters with a single space
decoded_script = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded_script)

# Print the decoded matrix script
print(decoded_script)