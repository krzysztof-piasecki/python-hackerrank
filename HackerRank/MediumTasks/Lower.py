number_of_squares = int(input())

array = [int(i) for i in input().split()]

streak = 0
best = 0
i = 1
while i < len(array):
    if array[i] <= array[i - 1]:
        streak += 1
        if streak > best:
            best = streak
    else:
        streak = 0
    i += 1
print(best)