from collections import Counter

amount = int(input())
array = input().split()
are_similar = False

array.sort()

previous_number = -2

for i in range(amount):
    number = int(array[i])
    if number - 1 == previous_number:
        are_similar = True
        break
    else:
        previous_number = number

print("YES" if are_similar == True else "NO")
