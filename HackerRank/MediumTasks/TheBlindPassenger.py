import math
number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    seat_number = int(input())
    if seat_number == 1:
        print("poor conductor")
    else:
        row = (seat_number + 4) / 5
        position = ""
        if row.is_integer():
            row -= 1
        if seat_number % 10 == 1 or seat_number % 10 == 2:
            position = " W L"
        elif seat_number % 10 == 3 or seat_number % 10 == 0:
            position = " A L"
        elif seat_number % 10 == 4 or seat_number % 10 == 9:
            position = " A R"
        elif seat_number % 10 == 5 or seat_number % 10 == 8:
            position = " M R"
        elif seat_number % 10 == 6 or seat_number % 10 == 7:
            position = " W R"
        row = math.floor(row)
        print(str(row) + position)