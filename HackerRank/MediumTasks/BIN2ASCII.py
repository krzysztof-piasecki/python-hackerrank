array = input().split()

for i in array:
    integer = int(i, 2)
    ascii_character = chr(integer)
    print(ascii_character, end="")