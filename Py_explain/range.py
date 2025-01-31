# range in py is in conhunction with a loop

print(range(1,11))
for number in range(1,11):
    print(number)
    
for number in range(1,11, 3):
    print(number)

# range of numbers 1 till 100 and add each number to the following number
# create a list with numbers in the range 1 till 100 (101)

sum_numbers = 0
for number in range(1,101):
    sum_numbers += number
print(sum_numbers)