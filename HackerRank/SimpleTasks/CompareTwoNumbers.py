amount_of_number = int(input())

i = 0

while amount_of_number > i:
    table_of_numbers = [int(i) for i in input().split(" ")]
    if table_of_numbers[0] > table_of_numbers[1]:
        print(str(table_of_numbers[0]) + "  is greater than  " + str(table_of_numbers[1]))
    elif table_of_numbers[0] < table_of_numbers[1]:
        print(str(table_of_numbers[0]) + "  is smaller than  " + str(table_of_numbers[1]))
    else:
        print("n is equal m:  " + str(table_of_numbers[0]))
    i += 1
