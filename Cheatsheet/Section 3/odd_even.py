# Check if a number is odd or even
print("Odd or Even")

# Step 1: Ask for a number
number = int(input("please enter a number => "))
# create an if condition using modulo
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"This is an odd number {number}")