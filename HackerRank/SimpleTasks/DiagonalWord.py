positions = int(input())

table = []
for i in range(positions):
    table.append(input())

new_word = ""
for i in range(positions):
    new_word += (table[i][i])
print(new_word)
