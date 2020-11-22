def sum_side(array):
    rightLeftEquation = array.split("=")
    left = rightLeftEquation[0]
    right = rightLeftEquation[1]
    sLeft = ""
    sRight = ""
    sumNumberLeft = 0
    sumXLeft = 0
    sumNumberRight = 0
    sumXRight = 0

    leftLength = len(left)
    rightLength = len(right)

    for j in range(rightLength if rightLength > leftLength else leftLength):
        if j < leftLength:
            characterLeft = left[j]
            if characterLeft.isdigit():
                sLeft += characterLeft
            elif characterLeft == "+" or characterLeft == "-":
                sumNumberLeft = int(sLeft) + sumNumberLeft if sLeft != "" else sumNumberLeft
                sLeft = characterLeft
            elif characterLeft == "x":
                if sLeft == "+" or sLeft == "-":
                    sumXLeft += int(sLeft + '1')
                    sLeft = ""
                else:
                    sumXLeft = int(sLeft) + sumXLeft if sLeft != "" else sumXLeft + 1
                    sLeft = ""
            if j == leftLength - 1 and left[j].isdigit():
                sumNumberLeft = int(sLeft) + sumNumberLeft if sLeft != "" else sumNumberLeft + 1
                sLeft = ""

        if j < rightLength:
            characterRight = right[j]
            if characterRight.isdigit():
                sRight += characterRight
            elif characterRight == "+" or characterRight == "-":
                sumNumberRight = int(sRight) + sumNumberRight if sRight != "" else sumNumberRight
                sRight = characterRight
            elif characterRight == "x":
                if sRight == "+" or sRight == "-":
                    sumXRight += int(sRight + '1')
                    sRight = ""
                else:
                    sumXRight = int(sRight) + sumXRight if sRight != "" else sumXRight + 1
                    sRight = ""
            if j == rightLength - 1 and right[j].isdigit():
                sumNumberRight = int(sRight) + sumNumberRight if sRight != "" else sumNumberRight + 1
                sRight = ""
    x = sumXRight - sumXLeft
    sumNumbers = sumNumberLeft - sumNumberRight
    return sumNumbers / x if x != 0 else "NO"


test_cases = int(input())

for i in range(test_cases):
    equation = input()

    print(sum_side(equation))


