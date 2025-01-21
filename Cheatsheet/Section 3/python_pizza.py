print("Welcome to python pizza deliveries")
size = input("Whatsize do you want S,M,L => ")
bill = 0
if size == "S":
    bill +=  15
    print(f"The size of your pizza is {size} and the cost is $15")
elif size == "M":
    bill += 20
    print(f"The size of your pizza is {size} and the cost is $20")
else:
    bill = 25
    print(f"The size of your pizza is {size} and the cost is $25")

peporroni = input("Do you want extra peperroni on your pizza? Y or N => ")
if peporroni == "Y":
    bill = 2
    print(f"The peporroni is added to your pizza and the cost is $2 extra")

else:
    costof__peporroni = int(0)
    print(f"No peporroni on your pizza today")
 
extra_cheese = input("Do you want extra cheese? Y or N => ")
if extra_cheese == "Y":
    bill += 1
    print(f"The extra_cheese is added to your pizza and the cost is $1 extra")

else:
    bill += int(0)
    print(f"No extra_cheese on your pizza today")

print(f"The total amount of your pizza => ${bill}")

# small pizza $15
# medium pizza $20
# large pizza $25
# pepperoni +$2
# extra cheese +$1