while int(input()) != 0:
    array = [int(i) for i in input().split()]

    i = 0
    k = 1
    work = 0
    amount = 0
    current_weight = 0
    for i in range(len(array)):
        current_weight += array[i]
        work += abs(current_weight)
    print(work)
