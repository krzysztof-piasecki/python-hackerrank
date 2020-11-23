array = [int(i) for i in input().split(" ")]
number_of_sums = int(input())

integer_sum = 0


for i in range(number_of_sums):
    array_of_first_and_last_integer = input().split(" ")
    first = int(array_of_first_and_last_integer[0])
    end = int(array_of_first_and_last_integer[1])

    while first <= end:
        integer_sum += array[first]
        first += 1

print(integer_sum)
