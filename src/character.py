# Character class
import random
import requests 
from race import Race
from background import Background, read_backgrounds

def parse_input(input) :
    ''' Parse input from Webpage form '''
    if input == "Random" :
        return ""
    else :
        return str(input).lower()
class Character:
    ''' This class should hold information about each character made using the generator '''

    def __init__(self, name_in):
        self.name = name_in
        self.stats = {"STR" : 0, "DEX": 0, "CON": 0, "INT": 0 , "WIS" : 0, "CHA" : 0}
        self.species = Race()
        self.background = Background()
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
            
    def generate(self,input_class,input_race,input_background) :
        ''' Function to generate a full character ''' 
        self.roll_stats()
        self.species.generate(input_race)
        backgrounds = read_backgrounds()
        self.background.generate(backgrounds,input_background)

        
    def output(self) :
        ''' Function to convert character to a dictionary for JSON output '''
        self.species = vars(self.species)
        self.background = vars(self.background)
        print("Checking background: ", self.background['name'])
        return vars(self)

