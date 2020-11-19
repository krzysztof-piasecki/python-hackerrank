number_of_integers = input()

array = [int(i) for i in input().split(" ")]

array.sort()

for i in array:
    print(i, end=" ")