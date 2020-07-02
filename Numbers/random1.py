import random
for i in range(10):
    #gives random float number in this range 1-100
    print(random.uniform(1,100))
    #gives random int with steps of 10
    print(random.randrange(2,100,10))
    #gives random int in range 1-100
    print(random.randint(1,100))
    if random.random() <= 0.5:
        print("Heads")
    else:
        print("Tails")

#use random.seed to maintain the random numbers generated after the seed so it can be replicated later

random.seed(10)
print(random.random())
print(random.random())

random.seed(10)
print(random.random())
print(random.random())

