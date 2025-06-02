# Exercise 1 :
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)


# Exercise 2 :
usernames = ["john 1990", "alberta1970", "magnola2000"]
chars = [len(item) for item in usernames]
print(chars)


# Exercise 3 :
user_entries = ['10', '19.1', '20']
user_numbers = [float(item) for item in user_entries]
print(user_numbers)


# Exercise 4 :
user_entries = ['10', '19.1', '20']
sum_of_numbers = sum(float(entry) for entry in user_entries)
print(sum_of_numbers)