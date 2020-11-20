string = input()

string_array = []
for i in range(len(string)):
    string_array.append(string[i])

steps = len(string_array)
i = 0
isProper = True
stack = []

while i < steps:
    start = string_array[i]

    if start == "{":
        stack.append("}")
    elif start == "(":
        stack.append(")")
    elif start == "[":
        stack.append("]")
    else:
        if not stack:
            isProper = False
            break
        elif start != stack.pop():
            isProper = False
            break
    i += 1
if stack:
    isProper = False
print(isProper)
