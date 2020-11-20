first_word = input()
second_word = input()

i = 0
taken_letters = 0
amount_of_letters = len(second_word)
is_true = True
while i < amount_of_letters:
    if first_word[i] != second_word[i]:
        if first_word[i + 1] != second_word[i]:
            is_true = False
            break
    i += 1
print("TAK" if is_true else "NIE")