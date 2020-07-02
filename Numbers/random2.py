import random
import string

moves = ["rock","paper","scissors"]
print(random.choice(moves))
#this will run choice 10 times
print(random.choices(moves, k=10))
#lets assume we have weights for diff colours
wheel = ['red','green','blue']
weights = [10,10,2]
print(random.choices(wheel,weights,k=10))
