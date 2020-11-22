s = input()
print(sum(int(i) for i in s.split() if int(i) > 0 and int(i)%2 == 0))
