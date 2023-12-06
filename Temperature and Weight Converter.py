#This is a temperature/weight converter

opperation = input("weight or temp:")
if opperation == "weight":
    weight = float(input("Enter your weight: "))
    unit = input("(kg/lb): ").upper()
    print(f"{weight}, {unit}")

    if unit == "KG" :
        weight *= 2.20462
        print(f"You are {round(weight,2)} LB")

    elif unit == "LB" :
        weight /= 2.20462
        print(f"You are {round(weight,2)} KG")

    else:
        print("Invalid unit")
        exit()

elif opperation == "temp":
    temp = float(input("Enter the temperature: "))
    unit = input("(C/F): ").upper()
    print(f"{temp}, {unit}")

    if unit == "C" :
        temp = (temp * 9/5) + 32
        print(f"{round(temp,2)} F")

    elif unit == "F" :
        temp = (temp - 32) * 5/9
        print(f"{round(temp,2)} C")
    else:
        print("Invalid unit")
        exit()

else:
    print("plz enter the right opperation symbol")
    exit()
