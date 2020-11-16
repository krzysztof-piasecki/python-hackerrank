numbers = input().split()


def numbers_add_function(numbers_table, iteration, added_numbers):
    if iteration < len(numbers_table):
        added_numbers += int(numbers_table[iteration])
        iteration += 1
        numbers_add_function(numbers_table, iteration, added_numbers)
    else:
        print(added_numbers)


i = 0
start_numbers = 0

numbers_add_function(numbers, i, start_numbers)
