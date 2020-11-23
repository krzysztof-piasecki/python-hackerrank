array = [int(i) for i in input().split(" ")]
number_of_sums = int(input())
dict = {}

for i in range(number_of_sums):
    integer_sum = 0
    array_of_first_and_last_integer = input().split(" ")
    first_indice = int(array_of_first_and_last_integer[0])
    second_indice = int(array_of_first_and_last_integer[1])

    first_in_dict = first_indice

    j = 0
    while first_indice <= second_indice:
        if (first_indice, second_indice) in dict:
            integer_sum += dict[(first_indice, second_indice)]
            break
        elif (first_indice, second_indice - j) in dict:
            integer_sum += dict[(first_indice, second_indice - j)]
            first_indice = second_indice - j + 1
            j = 0
        else:
            integer_sum += array[first_indice]
            dict[(first_in_dict,first_indice)] = integer_sum
            j += 1
            first_indice += 1
    print(integer_sum)



