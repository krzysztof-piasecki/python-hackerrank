matrix_size = [int(i) for i in input().split()]
seeked_string = input()
reverse_seeked_string = ""
for i in range(len(seeked_string)):
    reverse_seeked_string += seeked_string[len(seeked_string) - 1 - i]

n = matrix_size[0]
m = matrix_size[1]

is_found = False
horizontal_words = [""] * n
vertical_words = [""] * m
for i in range(n):
    given_line = input()
    horizontal_words[i] = given_line
    for j in range(m):
        vertical_words[j] += given_line[j]


for word in vertical_words:
    if seeked_string in word:
        is_found = True
        break
    if reverse_seeked_string in word:
        is_found = True
        break

for word in horizontal_words:
    if seeked_string in word:
        is_found = True
        break
    if reverse_seeked_string in word:
        is_found = True
        break

if not is_found:
    print("NO")
else:
    print("YES")