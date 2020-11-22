import time


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[1] = False
    return prime


test_cases = int(input())
array = []
highest = 0
for i in range(test_cases):
    array.append(int(input()))
    if array[i] > highest:
        highest = array[i]
support_array = SieveOfEratosthenes(highest)

for i in array:
    if support_array[i] == True:
        print("YES")
    else:
        print("NO")
