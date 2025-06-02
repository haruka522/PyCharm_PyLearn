# Exercise 1:
water_temperature = input("Enter the water temperature: ")
def water_state(temperature):
    if temperature <= 0:
        return "solid"
    elif 100 > temperature > 0:
        return "liquid"
    else:
        return "gas"

water_temp= water_state(int(water_temperature))
print(water_temp)


# Exercise 2:
Freezing_point = 0
Boiling_point = 100

def water_state2(temperature):
    if temperature <= Freezing_point:
        return "solid"
    elif Boiling_point > temperature > Freezing_point:
        return "liquid"
    else:
        return "gas"


# Exercise 3:
