import math
number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    table = [int(i) for i in input().split()]
    amount = table[0]

    j = 1
    gdc_sum = 0
    while j <= amount:
        k = j + 1
        while k <= amount:
            gdc_sum += math.gcd(table[j], table[k])
            k += 1
        j += 1
    print(gdc_sum)
