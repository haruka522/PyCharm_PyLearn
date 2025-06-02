
# Exercise 1

rate = 2

dollars = float(input("Enter the amount of dollars: "))
euros = dollars * rate
print(euros)


# Exercise 2

ranking = ['John', 'Sen', 'Lisa']
rank = int(input("Enter the rank: ")) - 1
name = ranking[rank]
print(name)


# Exercise 3

new_ranking = ['John', 'Sen', 'Lisa']
new_name = input("Enter a name: ")
new_rank = new_ranking.index(new_name) + 1
print(new_rank)


# Exercise 4

color_codes = ((1,2,3), (4,5,6), (7,8,9))


# Exercise 5

cars = ['toyota', 'honda', 'nissan']
new_car = input("Enter a new car: ")
cars.append(new_car)
print(cars)