s = input()
print(sum(i*i for i in range(int(s.split()[0]), (int(s.split()[1])+1))))
