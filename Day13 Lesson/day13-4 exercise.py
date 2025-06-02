# Exercise 1 :
birth_year = input("Enter your birt year: ")

def get_age(birth_year, current_year = 2025):
    age = current_year - int(birth_year)
    return age
try:
    age = get_age(birth_year)
    print(age)
    if age < 18:
        print("You are too young.")
    elif age > 18 and age < 65:
        print("You are an adult.")
    elif age > 65:
        print("You are an elder.")
    elif age > 120:
        print("You are too old.")
    else:
        print("Are you an alien?")
except:
    print("Invalid input, only numbers are allowed")
    
    
# Exercise 2 :
team_members = "John, Lisa, Allen, Teresa"
def get_team_members(team_members):
    team_members_list = team_members.split(", ")
    return team_members_list

team = get_team_members(team_members)
print(team)


# Exercise 3 :
square = input("Enter a number to get its square area: ")
def get_square(square):
    square_area = int(square) * int(square)
    return square_area
try:
    area = get_square(square)
    print(area)
except:
    print("Invalid input, only numbers are allowed")
    

# Exercise 4 :
input_temperature = input("Enter a temperature in Celsius: ")
def get_temperature(input_temperature):
    if input_temperature > 30:
        message = "It's hot"
    elif input_temperature < 10:
        message = "It's cold"
    else:
        message = "It's ok"
    return message
try:
    temperature = get_temperature(input_temperature)
    print(temperature)
except:
    print("Invalid input, only numbers are allowed")
    

# Exercise 5 :
input_password = input("Enter a password: ")

def check_password(input_password):
    if len(input_password) < 8:
        message = "Password is too short"
    elif len(input_password) > 16:
        message = "Password is too long"
    else:
        message = "Password is valid"
    return message
try:
    password = check_password(input_password)
    print(password)
except:
    print("Invalid input, only numbers are allowed")