import random as rand

class Dice:
    def __init__(self, color):
        self.color = color
        self.value = 0

    def roll(self):
        self.value = rand.randint(1,6)