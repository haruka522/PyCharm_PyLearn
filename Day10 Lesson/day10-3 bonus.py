try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    # if condition is not met, exit the program. if condition is met, continue with the program.
    # if condition can also work without else or elif
    if width <= 0 or length <= 0:
        print("Invalid input. Please enter positive numbers.")
        exit()
    if width == length:
        print("This is a square, not a rectangle.")
        exit()
        
        # don't use exit() with message in vs code
        # exit("This is a square, not a rectangle.")
        
    area = width * length

    print("The area of the rectangle is", area)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    

# if vs try-except
# if is used for conditional statements
# try-except is used for error handling