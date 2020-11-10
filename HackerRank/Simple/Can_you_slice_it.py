lowest = -1
highest = -1
table = [int(i) for i in input().split(" ")]
for x in table:
    if x > highest or highest == -1:
        highest = x
    if x < lowest or lowest == -1:
        lowest = x
table.sort()
amount = highest - lowest

i, j = 0, 0
step = 1
while amount > i:
    isSlicable = True
    while len(table) > (j + 1):
        if table[j + 1] - table[j] != step:
            isSlicable = False
        j += 1
    j = 0
    i += 1
    step += 1
    if isSlicable:
        break
try:
    t = table[1]
except IndexError:
    isSlicable = True
print(isSlicable)
