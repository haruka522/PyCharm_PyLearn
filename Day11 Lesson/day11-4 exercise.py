# Exercise 1 :

def max_grade(x):
    max_mark = max(x)
    return max_mark

grades = [9.1, 8.8, 7.5]
print(max_grade(grades))


# Exercise 2 :

def max_minGrade(x):
    max_mark = max(x)
    min_mark = min(x)
    return max_mark, min_mark

grades2 = [9.1, 8.8, 7.5]
max_min = max_minGrade(grades2)
print(max_min, type(max_min))



# Exercise 3 :

def max_minGrade2(x):
    max_mark = max(x)
    min_mark = min(x)
    messsage = f"The max grade is {max_mark} and the min grade is {min_mark}"
    y = [max_mark, min_mark, messsage]
    return y

grades3 = [9.1, 8.8, 7.5]
max_min2 = max_minGrade2(grades3)
print(max_min2, type(max_min2))
