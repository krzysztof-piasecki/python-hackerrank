import math
number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    table = [int(i) for i in input().split(" ")]
    first_paycheck, mars_money = table[0], table[1]
    if first_paycheck == mars_money:
        print(1)
    else:
        number_of_work_days = math.log((mars_money/first_paycheck)+1, 2)
        print(math.ceil(number_of_work_days))