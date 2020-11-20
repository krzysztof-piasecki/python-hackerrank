def howManyEndings(word, i, dict, count):
    if i < len(word):
        if word[i] in dict:
            dict[word[i]] += 1
            count += dict[word[i]]
            i += 1
            howManyEndings(word, i, dict, count)
        else:
            dict[word[i]] = 1
            count += 1
            i += 1
            howManyEndings(word, i, dict, count)
    else:
        print(count)


string = list(input())
dict = {}
first_iteration = 0
second_iteration = 0
first_count = 0
howManyEndings(string, first_iteration, dict, first_count)
