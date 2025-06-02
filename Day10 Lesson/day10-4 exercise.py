# exercise 1 :
try:
    total_value = float(input("Enter the total value: "))
    value = float(input("Enter the value: "))

    result = (value / total_value) * 100

    print("The percentage is: ", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
print()

# exercise 2 :
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("The result of division is:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print()

# exercise 3 :

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)