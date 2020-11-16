table = [int(i) for i in input().split(" ")]
john = int(table[0])
betty = int(table[1])

if john > betty:
    print("John")
elif betty > john:
    print("Betty")
else:
    print("NOBODY")
