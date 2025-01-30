# Rock paper siccors game
# step1:  Start with welcome tekst
# step2: create variable for rock,paper and siccors
# step3: ask player to make a choise
# step4: computer choise, create a list and random choose from this list rock, paper , siccors
# step5: compare players chise with computer choise and print the winner.


import random


# Welcome tekst
print("Let\'s play a game of ROCK, PAR or SICCORS")

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art for Paper
Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# ASCII art for Scissors
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Display the symbols
print("Rock:", Rock)
print("Paper:", Paper)
print("Scissors:", Scissors)    

# Ask player to make a choise

players_choise = input("please make your choise and enter here => ")
print(f"Players choise is {players_choise}")

# computer choise, create a list and random choose from this list rock, paper , siccors
list_of_symbols = ["Rock","Paper", "Siccors"]
print(f"Computer choise is {random.choice(list_of_symbols)}")

