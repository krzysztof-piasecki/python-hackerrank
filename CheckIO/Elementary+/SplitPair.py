def split_pairs(a):
    split_strings = []
    n = 2
    for index in range(0, len(a), n):
        split_strings.append(a[index: index + n])
    if len(a) % 2 != 0:
        split_strings[len(split_strings) - 1] = split_strings[len(split_strings) - 1] + "_"
    return split_strings


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
