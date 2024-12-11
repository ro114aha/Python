# # mathematic operations in python

# # PEMDAS = order of calculation

# # Parentheses ()
# print(2*(4+6))
# print((2*4)+6)

# # Exponents
# print(2**2)

# # Multiply and Division equal
# print(2*2/4)
# print(2/4*2)

# # Addition/Subtraction
# print((2+2)-(2+2))

# # Specials
# print(2/2)
# print(type(2/2))
# print(2//2)
# print(type(2//2)) # remove everything behind the comma

# debug to understand the order
print(3*(3 + 3)/3 -3)

# BMI Calculation
height = 1.86
weight = 101
#formular= weight divided by the person's height squared
print(type(height))
#test height squared
bmi = (height**2)
print(bmi)
#complete formular add weight
bmi = weight / (height ** 2)
print(bmi)

# floor vs round
print(int(bmi)) # this remove numbers afte rcomma
print(round(bmi)) # this wil round the number 
print(round(bmi,2)) # rounds the number with x-digits behind the comma
print(round(bmi,3)) # rounds the number with x-digits behind the comma
