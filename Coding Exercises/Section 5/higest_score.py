import random

#higest score using build in function max
#higst score calculate by using for
# Create a list of 10 random numbers between 0 and 100
# random_numbers = [random.randint(0, 100) for _ in range(10)]
# print(random_numbers)

higest_score = [73, 74, 76, 25, 89, 20, 18, 80, 71, 96]

print(sum(higest_score))
print(max(higest_score))

max_score = 0
for number in higest_score:
    if number > max_score:
        max_score = number
print(max_score)




    