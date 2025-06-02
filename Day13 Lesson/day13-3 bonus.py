feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    # message = f"{feet} feet and {inches} inches is equal to {meters} meters"
    return meters

try:
    parsed = parse(feet_inches)
    result = convert(parsed["feet"], parsed["inches"])
    print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")
    if result < 1:
        print("Kid is too small.")
    else:
        print("Kid can use the slide.")
except IndexError:
    print("Invalid input. Please enter feet and inches separated by a space.")
except ValueError:
    print("Invalid input. Please enter valid numbers for feet and inches.")
