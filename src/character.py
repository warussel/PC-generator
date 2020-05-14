# Character class
import random
import requests 
from race import Race

class Character:
    ''' This class should hold information about each character made using the generator '''

    def __init__(self, name_in):
        self.name = name_in
        self.stats = {"str" : 0, "dex": 0, "con": 0, "wis": 0 , "int" : 0, "cha" : 0}
        self.species = Race()
        print("Creating character: ", self.name)

    def roll_stats(self) :
        '''Function to generate random stats'''
        keys = list(self.stats)
        for i in range (6) :
            # Roll 4d6, drop the lowest
            dice = [] 
            for j in range (4) :
                dice.append(random.randint(1,6))
            dice.remove(min(dice))
            self.stats[keys[i]] = sum(dice)
        print("Random Stats = ", self.stats)
            
    def generate(self) :
        ''' Function to generate a full character ''' 
        self.roll_stats()
        self.species.generate()
        


