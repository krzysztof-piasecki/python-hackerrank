test_cases = int(input())

array = []
count = 0
anagrams = {}
for i in range(test_cases):
    string = sorted(input())
    final_version = "".join(string)
    if final_version in anagrams:
        anagrams[final_version] += 1
        count += anagrams[final_version]
    else:
        anagrams[final_version] = 0
print(count)