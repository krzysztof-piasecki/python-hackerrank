first_line = [int(i) for i in input().split(" ")]
n = first_line[0]
m = first_line[1]

second_line = [int(i) for i in input().split(" ")]

for i in range(m):
    array = [int(j) for j in input().split(" ")]
    first_swap_number = second_line[array[0]]
    second_swap_number = second_line[array[1]]

    second_line[array[0]] = second_swap_number
    second_line[array[1]] = first_swap_number

for i in second_line:
    print(i, end=" ")