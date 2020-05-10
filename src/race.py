# Race class for potential player races (species, i.e. elf, dwarf, human)
import random
from api import get_data

class Race :
    ''' A class representing a character's species '''

    def __init__(self) :
        ''' Initialize member variables to default values '''
        self.name = ""
        self.scores = {"STR" : 0, "DEX": 0,"INT" : 0,"CON" : 0,"WIS" : 0,"CHA" : 0 }
        self.speed = 0 
        self.languages = []
        self.size = ""

    def generate(self,r_in="") :
        ''' Generate a species using the specified race, or randomly chosen if none is given'''

        endpoint = "api/races/"
        if r_in == "" :
            # Grab all races JSON
            data = get_data(endpoint)["results"]
            races = list()

            # Select a random race
            for elt in data :
                races.append(elt["index"])
                print("Race: ", elt["index"])
            self.name = races[random.randint(0,len(races) - 1)]
            print("Creating random race: ", self.name)
        
        else :
            # Select the input race
            self.name = r_in
            print("Creating race: ", self.name)
        
        # Grab this character's race JSON
        endpoint += (self.name + "/")
        data = get_data(endpoint)

        # Set data from JSON
        self.speed = data["speed"]
        self.size = data["size"]
        for elt in data["languages"] :
            self.languages.append(elt["name"])
        for elt in data["ability_bonuses"] :
            self.scores[elt["name"]] = elt["bonus"]
            print("Bonus: ", elt["name"], " = ", elt["bonus"])


