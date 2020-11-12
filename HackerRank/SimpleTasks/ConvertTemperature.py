def check_celsius(convert):
    if convert < (-273.15):
        print("NO")
        return False
    else:
        return True


def check_kelvin(convert):
    if convert < (0):
        print("NO")
        return False
    else:
        return True


def check_fahrenheit(convert):
    if convert < (-459.67):
        print("NO")
        return False
    else:
        return True


def convert_celsius_to_kelvin_fahrenheit(convert, second_format):
    if second_format == "Kelvin":
        convert += 273.15
    else:
        convert = 32 + (9 / 5) * convert
    print("{:.2f}".format(convert))


def convert_kelvin_to_celsius_fahrenheit(convert, second_format):
    if second_format == "Celsius":
        convert -= 273.15
    else:
        convert = 32 + (9 / 5) * (convert - 273.15)
    print("{:.2f}".format(convert))


def convert_fahrenheit_to_celsius_kelvin(convert, second_format):
    if second_format == "Kelvin":
        convert = ((5 / 9) * (convert - 32)) + 273.15
    else:
        convert = (5 / 9) * (convert - 32)
    print("{:.2f}".format(convert))


amount = int(input())

i = 0
while amount > i:
    table = [j for j in input().split(" ")]
    degree = float(table[0])
    firstFormat = table[1]
    secondFormat = table[2]

    if firstFormat == "Celsius":
        if check_celsius(degree):
            convert_celsius_to_kelvin_fahrenheit(degree, secondFormat)
    if firstFormat == "Kelvin":
        if check_kelvin(degree):
            convert_kelvin_to_celsius_fahrenheit(degree, secondFormat)
    if firstFormat == "Fahrenheit":
        if check_fahrenheit(degree):
            convert_fahrenheit_to_celsius_kelvin(degree, secondFormat)
    i += 1
