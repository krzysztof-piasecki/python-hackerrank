import math

number_of_cities = int(input())

cities = {}

for i in range(number_of_cities):
    support_array = input().split()
    cities[support_array[0]] = [int(support_array[1]), int(support_array[2])]
city_order = input().split()

trip = 0

for i in range(len(city_order) - 1):
    firstCityX = cities.get(city_order[i])[0]
    firstCityY = cities.get(city_order[i])[1]
    secondCityX = cities.get(city_order[i + 1])[0]
    secondCityY = cities.get(city_order[i + 1])[1]

    trip += math.sqrt(((secondCityX - firstCityX)*(secondCityX - firstCityX)) + ((secondCityY - firstCityY)*(secondCityY - firstCityY)))

firstCityX = cities.get(city_order[0])[0]
firstCityY = cities.get(city_order[0])[1]
secondCityX = cities.get(city_order[len(city_order) - 1])[0]
secondCityY = cities.get(city_order[len(city_order) - 1])[1]

trip += math.sqrt(((secondCityX - firstCityX)*(secondCityX - firstCityX)) + ((secondCityY - firstCityY)*(secondCityY - firstCityY)))
print(trip)
