sentence = input()
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

for i in vowels:
    sentence = sentence.replace(i, "")
for j in vowels:
    sentence = sentence.replace(j.upper(), "")
print(sentence)
