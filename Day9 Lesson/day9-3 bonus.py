password = input("Enter new password: ")

result = []
if len(password) >= 8:
    result.append("True")
else:
    result.append("False")

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)
        
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result.append(uppercase)
        
print(result) 

# all() function returns True if all items in an iterable are true, otherwise it returns False.
# print(all(result))

if all(result):
    print("Strong Password")
else:
    print("Weak Password")