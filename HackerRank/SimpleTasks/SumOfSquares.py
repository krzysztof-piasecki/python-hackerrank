table = [int(i) for i in input().split(" ")]

value = 0
i = table[0]
while table[1] >= i:
    value += i * i
    i += 1
print(value)
