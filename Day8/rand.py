import random

#random number between 0 and 1
for i in range(3):
    print(random.random())
    
#random number between a range
for i in range(3):
    print(random.randint(10, 20))
    
#randomly pick from a list
names = ["John", "Shy", "Joe", "Gabe"]
lead = random.choice(names)
print(lead)