def find_highest_sum(_support_table, _highest_sum):
    _current_sum = 0
    for _x in _support_table:
        _current_sum = max(_x, _current_sum + _x)
        _highest_sum = max(_highest_sum, _current_sum)
    return _highest_sum


size = int(input())
matrix = []
support_table = []

for x in range(size):
    table = [int(i) for i in input().split(" ")]
    matrix.append(table)

highest_sum = -1000
i = 0
y = 0
z = 0
next_iteration = True
for x in range(size):
    while y < size:
        while z < size:
            if next_iteration:
                support_table.append(matrix[y][z])
            else:
                support_table[i] = support_table[i] + matrix[y][z]
            i += 1
            z += 1
        next_iteration = False
        i = 0
        highest_sum = max(highest_sum, find_highest_sum(support_table, highest_sum))
        y += 1
        z = 0
    next_iteration = True
    support_table = []
    y = x + 1
print(highest_sum)
