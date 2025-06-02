feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    # split the string into two parts using the split() method
    # the split() method returns a list of substrings
    # in here we are splitting the string into two parts using the space as the delimiter
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    
    meters = feet * 0.3048 + inches * 0.0254
    message = f"{feet} feet and {inches} inches is equal to {meters} meters"
    return meters

# print(convert(feet_inches))
try:
    result = convert(feet_inches)
    if result < 1:
        print("Kid is too small.")
    else:
        print("Kid can use the slide.")
except IndexError:
    print("Invalid input. Please enter feet and inches separated by a space.")
except ValueError:
    print("Invalid input. Please enter valid numbers for feet and inches.")

