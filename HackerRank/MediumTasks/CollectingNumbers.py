matrix_size = int(input())

matrix = []

for i in range(matrix_size):
    array = [int(i) for i in input().split()]
    matrix.append(array)

i = 0
j = 0
k = 0

while j < matrix_size - 1:
    while k < matrix_size - 1:
        if j == 0:
            matrix[j][k + 1] += matrix[j][k]
            matrix[k + 1][j] = matrix[k + 1][j] + matrix[k][j]
        else:
            matrix[j][k + 1] += max(matrix[j][k], matrix[j-1][k+1])
            matrix[k + 1][j] += max(matrix[j][k], matrix[k+1][j-1])
        k += 1
    matrix[j + 1][j + 1] += max(matrix[j + 1][j], matrix[j][j + 1])
    k = j + 1
    j += 1
print(matrix[matrix_size-1][matrix_size-1])

