#function which shift letters according to given number
def lettershift(char, shift, ASCII_letters_start, ASCII_letters_end):
    if ord(char) - shift < ASCII_letters_start:
        letter = ASCII_letters_end - (shift - (ord(char) - ASCII_letters_start))
    else:
        letter = ord(char) - shift
    return letter


shift = int(input()) % 26
givenString = input()

# upper letters in ASCII 65 - 90
# lower letters in ASCII 97 -122

ASCII_upper_letters_start = 65
ASCII_upper_letters_end = 91
ASCII_lower_letters_start = 97
ASCII_lower_letters_end = 123

ASCII_values = []

for char in givenString:

    if char.isupper():
        startLetter = ASCII_upper_letters_start
        endLetter = ASCII_upper_letters_end
    else:
        startLetter = ASCII_lower_letters_start
        endLetter = ASCII_lower_letters_end

    ASCII_values.append(lettershift(char, shift, startLetter, endLetter))

for numbers in ASCII_values:
    print(chr(numbers), end='')
