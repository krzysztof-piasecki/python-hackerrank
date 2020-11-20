from collections import defaultdict

first_solution = {}
second_solution = {}
array = [int(i) for i in input().split(" ")]
n, x, y = array[0], array[1], array[2]

a = b = c = d = 0

count = 0
overall = 0

if n > 0 and x > 0 and y > 0:
    while n >= a:
        while n >= b:
            equation = (x*a*a + y*b*b)
            if equation in first_solution:
                first_solution[equation] += 1
            else:
                first_solution[equation] = 1
            b += 1
        a += 1
        b = 0
    while n >= c:
        while n >= d:
            second_equation = (x*c*c + y*d*d)
            if second_equation in second_solution:
                second_solution[second_equation] += 1
            else:
                second_solution[second_equation] = 1
            d += 1
        c += 1
        d = 0
    for x in second_solution:
        if x in first_solution:
            count += (first_solution[x] * second_solution[x])

print(count)
