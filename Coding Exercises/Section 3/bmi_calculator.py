weight = 105
height = 1.85

bmi = weight / (height ** 2)
print(bmi)

# 🚨 Do not modify the values above
# Write your code below 👇

# if esif else statement to determen 
# underweight <18,5 
# normal >18,5 =<24-9
# overweight >25 <=29.9

if bmi < 18.5:
    print("Your underweight")
elif bmi >18.5 and bmi <=24.9:
    print("Your weight is normal")
else:
    print("Your overweight")