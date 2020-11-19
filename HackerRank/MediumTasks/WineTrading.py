while int(input()) != 0:
    table = [int(i) for i in input().split()]

    i = 0
    k = 1
    work = 0
    amount = 0
    current_weight = 0
    while i < len(table):
        current_weight += table[i]
        work += abs(current_weight)
        i += 1
    print(work)
