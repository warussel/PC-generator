# Race class for potential player races (species, i.e. elf, dwarf, human)

class Race :
    ''' A class representing a character's species '''

    def __init__(self) :
        self.scores = {"str" : 0, "dex": 0,"int" : 0,"con" : 0,"wis" : 0,"cha" : 0 }
        self.speed = 0 
        self.languages = []
        self.size = ""
Race()