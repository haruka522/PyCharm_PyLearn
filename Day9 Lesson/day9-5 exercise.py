# Exercise 1 :

password = input("Enter a new password: ")

if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Your password is almost good enough")
else:
    print("Your password is weak")
    

# Exercise 2 :
day_temperatures = {'morning': 5.1, 'noon': 6.1, 'evening': 10.2}


# Exercise 3 :
day_temperatures2 = {'morning': (1.1 , 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}


# Exercise 4 :
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
new_letters = letters[1:4]
print(new_letters)


# Exercise 5 :
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
new_letters = letters[-3:]
print(new_letters)