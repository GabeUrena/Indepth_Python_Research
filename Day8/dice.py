import random

class Dice:
    
    def roll(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1, 6)
        return (dice1, dice2)


dice = Dice()
print(dice.roll())