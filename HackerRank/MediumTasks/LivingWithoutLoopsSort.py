def partitionhelper(x, j, pivot, i):
    if j < len(x) - 1:
        if x[j + 1] < pivot:
            x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
            i += 1
            j += 1
            return partitionhelper(x, j, pivot, i)
        j += 1
        return partitionhelper(x, j, pivot, i)
    else:
        return x, i, j, pivot


def quickmove(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        j = 0
        x, i, j, pivot = partitionhelper(x, j, pivot, i)
        x[0],x[i] = x[i],x[0]
        first_part = quickmove(x[:i])
        second_part = quickmove(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

def stringtoint(list, i):
    if i < len(list):
        list[i] = int(list[i])
        i += 1
        return stringtoint(list, i)
    else:
        return list

list = input().split()
i = 0

stringtoint(list, i)
quickmove(list)

print(*quickmove(list))
