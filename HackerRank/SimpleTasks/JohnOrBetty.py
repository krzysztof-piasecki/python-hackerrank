array = [int(i) for i in input().split(" ")]
john = int(array[0])
betty = int(array[1])

if john > betty:
    print("John")
elif betty > john:
    print("Betty")
else:
    print("NOBODY")
