# Exercise 1:

filenames = ['a.txt', 'b.txt', 'c.txt']

for i, j in enumerate(filenames):
    print(f"{i}-{j.capitalize()}.txt")
print()


# Exercise 2:

ips = ['100.122.133.105', '100.122.133.111']

for i, j in enumerate(ips):
    print(f"{i+1}-{j}")
user_input = int(input("Enter the index of the IP you want: "))
print(f"You chose {ips[user_input-1]}")
print()


# Exercise 3:

seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)