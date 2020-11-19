amount_of_number = int(input())

i = 0

while amount_of_number > i:
    array_of_numbers = [int(i) for i in input().split(" ")]
    if array_of_numbers[0] > array_of_numbers[1]:
        print(str(array_of_numbers[0]) + "  is greater than  " + str(array_of_numbers[1]))
    elif array_of_numbers[0] < array_of_numbers[1]:
        print(str(array_of_numbers[0]) + "  is smaller than  " + str(array_of_numbers[1]))
    else:
        print("n is equal m:  " + str(array_of_numbers[0]))
    i += 1
