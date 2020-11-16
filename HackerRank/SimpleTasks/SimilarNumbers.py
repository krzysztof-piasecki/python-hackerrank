from collections import Counter
amount = int(input())
array = input().split(" ")

counts = Counter()

previous_number = -2
are_similar = False

for i in range(amount):
    if int(array[i]) + 1 == previous_number:
        are_similar = True
        break
    previous_number = int(array[i])

print("YES" if are_similar == True else "NO")
