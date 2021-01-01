import math
def remove_at(i, s):
    return s[:i] + s[i+1:]


def check_palindrome(s, e):
    loop_range = math.floor((len(s) - 1) / 2)
    for i in range(int(loop_range)):
        if s[i].lower() != s[len(s) - 1 - i].lower():
            e += 1
            if e == 3:
                return "NO"

            if s[i].lower() == s[len(s) - 2 - i].lower():
                s = remove_at(len(s) - 1 - i, s)
                return check_palindrome(s, e)
            elif s[i + 1].lower() == s[len(s) - 1 - i].lower():
                s = remove_at(i, s)
                return check_palindrome(s,e)
    return "YES"


string = input()
errors = 0

print(check_palindrome(string, errors))