# if else condition
# check height 120

#Welcome to the RollerCoster
print("Welcome to the Rollercoaster")
# Step1: Ask for the height of the person
# make the input an integer
height = int(input("What is yout height in cm =>"))
print(height)
# Step2: Check if the height is above 120 cm with a if else statement
if height > 120:
    print(f"Your height is {height} Welcome to the rollercoaster")
else: 
    print(f"Your height {height} and is below the minimum height of 120 cm")