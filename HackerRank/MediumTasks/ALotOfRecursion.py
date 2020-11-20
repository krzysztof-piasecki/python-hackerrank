number = int(input())
array = [1, 1]

i = 1

while i < number:
    array.append(1 + array[i + 1 - array[array[i]]])
    i += 1

print(array.pop())