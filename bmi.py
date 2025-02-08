height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))

BMI = weight / (height/100)**2

print("Your BMI is:", BMI)

if BMI <= 18.4:
    print("You are very thin.")

elif BMI <= 22.9:
    print("You are getting healthy.")

elif BMI <= 26.9:
    print("You are healthy")

elif BMI <= 30.9:
    print("You are getting fat.")

elif BMI <= 34.9:
    print("You need to exercise.")

else:
    print("You are a planet.")