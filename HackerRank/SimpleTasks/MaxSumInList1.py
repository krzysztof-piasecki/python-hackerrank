table = [int(i) for i in input().split(" ")]

current_sum = 0
largest_sum = 0
for i in table:
    current_sum += i
    if current_sum < 0:
        current_sum = 0
    if current_sum > largest_sum:
        largest_sum = current_sum
print(largest_sum)