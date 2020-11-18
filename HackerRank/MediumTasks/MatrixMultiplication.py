first_size_array = [int(i) for i in input().split(" ")]
w1 = first_size_array[0]
h1 = first_size_array[1]

first_matrix = []

for i in range(h1):
    first_to_int_support_array = [int(i) for i in input().split(" ")]
    first_matrix.append(first_to_int_support_array)

second_size_array = [int(i) for i in input().split(" ")]
w2 = second_size_array[0]
h2 = second_size_array[1]

second_matrix = []

for i in range(h2):
    second_to_int_support_array = [int(i) for i in input().split(" ")]
    second_matrix.append(second_to_int_support_array)

final_matrix = [[0 for x in range(w2)] for y in range(h1)]

i = 0

while i < h1:
    j = 0
    while j < w2:
        count = 0
        k = 0
        while k < w1:
            count += (first_matrix[i][k] * second_matrix[k][j])
            k += 1
        print(count, end=" ")
        j += 1
    print()
    i += 1


