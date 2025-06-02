# Exercise 1 :
def liters_to_ml(liters):
    x =  liters * 1000
    return x


# Exercise 2 :

def strength(password):
    
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False
    
    digit = False
    uppercase = False
    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase
    
    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


# Exercise 3 :
def average(list):
    return sum(list) / len(list)


# Exercise 4 :
def total(n1, n2):
    return n1 + n2

# Exercise 5 :
def name_title(name):
    return f"hi {name.title()}"