def sequance(n,k, number):
    print(n, end=" ")
    if n - k != number:
        if n < 0:
            k = -k
        n -= k
        return sequance(n,k,number)
    else:
        print(number, end=" ")
        return n




array = input().split()
n = int(array[0])
k = int(array[1])
starting = n

sequance(n, k, starting)