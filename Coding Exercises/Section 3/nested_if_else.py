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
#Enter bill amount 
bill = 0
if height > 120:
    print("Your height is ok. Let's check your age")
    age =int(input("What is your age => "))
    if age <= 12:
        bill = 5
        print(f"The ticket price is ${bill}")
    elif age < 18:
        bill = 7
        print(f"The ticket price is ${bill}")
    else:
        bill = 12
        print(f"The ticket price is ${bill}")

# Ask if the want a photo of their ride
    wants_picture = input("Do you want an photo? Enter Y for yes or N for no =>")
    if wants_picture == "Y":
        bill += 3
        print(f"Total amount ${bill}")
    else:
        print(f"Total amount ${bill}")
    
    
else: 
    print(f"Your height is {height} and is below the minimum height of 120 cm")