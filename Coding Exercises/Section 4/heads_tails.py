# heads or tails
import random

head_or_tail = input("Heads or tail what\'s gonna be ? => ")
print(head_or_tail)
result= random.choice(["heads", "tail"])
print(result)
if head_or_tail == result:
    print(f"Your choice is {head_or_tail} You win !")
else:
    print(f"Your choice is {head_or_tail} You loose !")
