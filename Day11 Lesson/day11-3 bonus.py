def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    
    average_local = sum(values) / len(values)
    return average_local
    
    

average = get_average()
print("average value: ", average )





print()

print("3.2\n")

# when you use int() or float() to convert a string, the string has to be a valid number
# \n will be removed after the conversion
print(int("3\n"))
print(float("3.5\n"))

# this will show error, cuz that "3.8" is string, not number and it has decimal
# print(int("3.8"))

# so you can't use int() to convert it to int, but you can use float() to convert it to float
# then you can use int() to convert it to int, before converting it to int, if you want to round the number, you can use round()
# normally, after rounding, the number will be integer, but in some cases, when you want to round the number but keep the decimal part, it will be float

my_number = "5.6\n"
print(int(float(my_number)))

rounded_number = round(float(my_number))
print(type(rounded_number), rounded_number)

# round(number,  decimal_places)
rounded_number2 = round(float(8.749), 2)
# this will print    <class 'float'> 8.75
print(type(rounded_number2), rounded_number2)


