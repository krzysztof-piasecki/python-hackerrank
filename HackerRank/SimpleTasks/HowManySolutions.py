table = [int(i) for i in input().split(" ")]
n, x, y = table[0], table[1], table[2]

solution = []
i = 0

a = b = c = d = 0

count = 0
overall = 0
while n >= a:
    while n >= b:
        while n >= c:
            while n >= d:
                overall += 1
                solution.append(str(a) + " " + str(b) + " " + str(c) + " " + str(d))
                if x*a*a + y*b*b == x*c*c + y*d*d:
                    count += 1
                d += 1
            c += 1
            d = 0
        b += 1
        c = 0
        d = 0
    a += 1
    b = 0
    c = 0
    d = 0
print(count)
