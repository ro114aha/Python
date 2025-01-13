# nested if else condition
# check height 120
# check age >=7

#Welcome to the RollerCoster
print("Welcome to the Rollercoaster")
# Step1: Ask for the height of the person
# make the input an integer
height = int(input("What is yout height in cm =>"))
print(height)
# Step2: Ask for the age of the person
# make the input an integer
# Step2: Check if the height is above 120 cm with a if else statement
if height > 120:
    print("Your height is ok. Let's check your age")
    age =int(input("What is your age => "))
    if age <= 12:
        print("Please pay $5")
    elif age < 18:
        print("PLease pay $7")
    else:
        print("Please pay $12")
else: 
    print(f"Your height is {height} and is below the minimum height of 120 cm")