import string
import random
# Create a simple password generator
#LETTERS
# Step 1 make a list of letters
letters = list(string.ascii_letters)
#Step 2 Ask user how many letters the password should contain
how_many_letters = input("How many letters do you want for your password? enter here :")
# Convert input to integer
how_many_letters = int(how_many_letters)
# Select the number of random letters specified by the user
selected_letters = random.choices(letters, k=how_many_letters)
#NUMBERS
# Step 1 make a list of numbers
numbers = list(range(1, 12))
#Step 2 Ask user how many numbers the password should contain
how_many_numbers = int(input("How many numbers do you want for your password? enter here :"))
# how_many_numbers = int(how_many_numbers)
#Step3 Select the number of random numbers specified by the user
selected_numbers = random.choices(numbers, k=how_many_numbers)
#SYMBOLS
# Step 1 make a list of symbols
symbols = list("!@#$%^&*()-_=+[]{}?/")
#Step 2 Ask user how many symbols the password should contain
how_many_symbols = input("How many symbols do you want for your password? enter here :")
how_many_symbols = int(how_many_symbols)
#Step3 Select the number of random symbols specified by the user
selected_symbols = random.choices(symbols, k=how_many_symbols)
# Combine the selected letters, numbers, and symbols into one list
password_list = selected_letters + selected_numbers + selected_symbols
# Shuffle the combined list to ensure randomness
random.shuffle(password_list)
# Convert the list to a string
password = ''.join(map(str, password_list))
# Print the generated password
print(f"The generated password is: {password}")





