import math
number_of_test_cases = int(input())


for i in range(number_of_test_cases):
    number = int(input())
    floor_2 = math.floor(number/2)
    while floor_2 > 0:
        if math.gcd(floor_2, number) == 1:
            print(floor_2)
            break
        else:
            floor_2 -= 1