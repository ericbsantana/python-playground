import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
p = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for i in range(m):
    for j in range(n):
        p.append(matrix[j][i])

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', ''.join(p)))
