table = [int(i) for i in input().split(" ")]
table_of_first_and_last_integer= input().split(" ")

first = int(table_of_first_and_last_integer[0])
end = int (table_of_first_and_last_integer[1])

integer_sum = 0
while first <= end:
    integer_sum += table[first]
    first += 1

print(integer_sum)
