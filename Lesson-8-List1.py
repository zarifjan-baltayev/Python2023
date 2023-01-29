cities = ['New York', 'Moscow', 'new delhi', 'Simferopol', 'Toronto']
print(cities)
print(len(cities))

print(cities[0])
print(cities[-1])
print(cities[2].title())
print(cities[2].upper())

cities[2] = 'Tula'
print(cities)

cities.append('Kursk')
cities.append('Yalta')
print(cities)

cities.insert(0, 'Izmir')
print(cities)
cities.insert(2, 'Feodosiya')
print(cities)

del cities[-1]
print(cities)

cities.remove('Tula')
print(cities)

deleted_city = cities.pop()
print("*********")
print(cities)
print("Deleted city is: " + deleted_city)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

print("+++++")
cities.reverse()
print(cities)
