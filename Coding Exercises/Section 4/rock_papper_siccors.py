# Rock paper siccors game
# step1:  Start with welcome tekst
# step2: create variable for rock,paper and siccors
# step3: ask player to make a choise



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

# step3: ask player to make a choise

players_choise = input("please make your choise and enter here => ")
print(f"Players choise is {players_choise}")