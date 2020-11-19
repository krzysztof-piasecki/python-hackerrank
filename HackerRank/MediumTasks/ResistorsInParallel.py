amount_of_numbers = int(input())

array = [int(i) for i in input().split()]
sum = 0

for i in array:
    sum += (1/i)

print(1/sum)