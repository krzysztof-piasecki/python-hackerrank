lowest = -1
highest = -1
array = [int(i) for i in input().split(" ")]
for x in array:
    if x > highest or highest == -1:
        highest = x
    if x < lowest or lowest == -1:
        lowest = x
array.sort()
amount = highest - lowest

i, j = 0, 0
step = 1
while amount > i:
    is_slicable = True
    while len(array) > (j + 1):
        if array[j + 1] - array[j] != step:
            is_slicable = False
        j += 1
    j = 0
    i += 1
    step += 1
    if is_slicable:
        break
try:
    t = array[1]
except IndexError:
    is_slicable = True
print(is_slicable)
