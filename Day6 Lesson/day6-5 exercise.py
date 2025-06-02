
# Exercise 1 :
# there's a nameslist.txt file. The existing code opens that file in read mode. Below that code, please read the file content and print out the content.

# file = open("nameslist.txt", "r")
# names = file.read()
# print(names)


# Exercise 2 :
# You should create a program that reads the nameslist.txt file, converts the first letter of each word to uppercase and prints out the converted text.

# file = open("nameslist.txt", "r")
# names = file.readlines()
# for name in names:
#     name = name.capitalize()
#     print(name)
    

# Exercise 3 :
# Write a program that reads the essay.txt file and returns the number of characters contained in the file.

# file = open("essay.txt", "r")
# essay = file.read()
# print(len(essay))


# Exercise 4 :
# Use Python to create a file with name file.txt and write the text snail there.

# file = open("file.txt", "w")
# file.write("snail")
# file.close()


# Exercise 5 :
# file = open("data.txt", 'w')
# file.write("100.12\n")
# file.write("111.23\n")
# file.close()


# Exercise 6 :

user_prompt = input("Add a new car: ") + "\n"
user_prompt = user_prompt.strip()

file = open("cars.txt", "r")
cars = file.readlines()
file.close()

cars.append(user_prompt)
file = open("cars.txt", "w")
file.writelines(cars)
file.close()

car_name = ''
for car in cars:
    car = car.strip('\n')
    car_name += car + " "
print(car_name)


# Exercise 7 :

filenames = ['a_file.txt', 'b_file.txt', 'c_file.txt']
for filename in filenames:
    file = open(filename, "w")
    file.write("Hello")
    file.close()


# Exercise 8 :
text_files = ['a.txt', 'b.txt', 'c.txt']

for filename in text_files:
    file = open(filename, "r")
    content = file.read()
    file.close()
    print(content)