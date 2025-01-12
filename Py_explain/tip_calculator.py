# Welcome to the Tip Calculator
print("Welcome to the Tip calculator")
# steps 1 : Ask for total Bill should be a float
amount_of_bill = float(input("What is the total amount of the bill? =>€ "))
print(amount_of_bill)
# step 2: : How much tip would you like to give? 10,12 or 15 ?
tip = float(input("How many percentage tip would you like to give? => "))
# step 2b; calculate the tip
calculate_tip = tip/100
print(calculate_tip)

#step3 Add tip to amount of the bill
total = float(amount_of_bill *(1+calculate_tip))
print(total)

# step 3: How many people split the Bill? 7
split=int(input("How many people split the bill? =>"))
print(split)
# step 4: Calculate what every person should pay
pay = int(total/split)
# step 5 : Each person should pay : 
print(f"Every person should pay => €{float(pay)}")
