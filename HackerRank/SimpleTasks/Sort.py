number_of_integers = input()

table = [int(i) for i in input().split(" ")]

table.sort()

for i in table:
    print(i, end=" ")