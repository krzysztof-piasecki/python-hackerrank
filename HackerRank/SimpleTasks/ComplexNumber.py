import re
import math

#getting numbers from complex numbers
complex_number = re.split(' \+ |j',input())

real_number = int(complex_number[0])
imaginary_number = int(complex_number[1])
modulus = math.sqrt(real_number * real_number + imaginary_number * imaginary_number)

if real_number != 0:
    if real_number < 0 <= imaginary_number:
        argument = math.atan(imaginary_number/real_number) + math.pi
    elif real_number < 0 and imaginary_number <= 0:
        argument = math.atan(imaginary_number / real_number) - math.pi
    else:
        argument = math.atan(imaginary_number / real_number)

elif real_number == 0:
    if imaginary_number > 0:
        argument = math.pi/2
    else:
        argument = -math.pi/2
print(modulus)
print(argument)
