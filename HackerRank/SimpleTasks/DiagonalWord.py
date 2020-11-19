positions = int(input())

array = []
for i in range(positions):
    array.append(input())

new_word = ""
for i in range(positions):
    new_word += (array[i][i])
print(new_word)
