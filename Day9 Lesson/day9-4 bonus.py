password = input("Enter new password: ")

# {} is a dictionary. In dictionary, we have key and value {'key': 'value', 'key2': 'value2', 'key3': 'value3', etc.}
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit
        
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["upper-case"] = uppercase
        
print(result) 

# this will always return true cuz it will only check the key of the dictionary.
print(all(result))

# this will return true if all the values of the keys are true, if not, it will return false.
print(all(result.values()))

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")