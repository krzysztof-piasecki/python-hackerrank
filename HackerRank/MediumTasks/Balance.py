import math
number_amount = int(input())

array = [int(i) for i in input().split()]
average = sum(array) / 2
sum1 = 0
difference = 0
for i in array:
    sum1 += i
    if sum1 > average:
        difference = 2*(abs(sum1 - average)) if abs(sum1 - average) < abs(sum1 - i - average) else 2*abs(sum1 - i - average)
        print(int(difference))
        break
