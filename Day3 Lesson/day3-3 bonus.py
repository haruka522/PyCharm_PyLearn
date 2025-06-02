
cars = ['bmw', 'audi', 'toyota', 'subaru']

for car in cars:
    print(car.title())

print()

# list's index start from 0, so index 1 is "audi" and index 3 is "subaru"
print(cars[1], cars[3])

# list's index can be changed
cars[1] = 'benz'
print(cars[1])

# you can also use index method with argument to find the index number of a value
print( "index number of toyota in list of cars: " , cars.index('toyota'))

print()

for character in "Hello":
    print(character)
    
print("Bye Bye!")