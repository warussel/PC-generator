# Background class for character backgrounds
import json
import os
import sys
import random

class Background :
    ''' A class representing a character's background '''

    # TODO: remove input from this function. __init__ should use default values
    def __init__(self) :
        self.name = ""
        self.skills = []
        self.tools = []
        self.equipment = []
        self.feature = ""
        self.num_lang = 0

    def set_val(self,name_in,skills_in,tools_in,equip_in,lang_in,feature_in) :
        self.name = name_in
        self.skills = skills_in
        self.tools = tools_in
        self.equipment = equip_in
        self.feature = feature_in
        self.num_lang = lang_in

    def generate(self,backgrounds,b_in="") :

        index = random.randint(0,len(backgrounds) - 1)
        for i in range(len(backgrounds)) :
            if backgrounds[i].name == b_in :
                index = i

        self.name = backgrounds[index].name
        self.skills = backgrounds[index].skills
        self.tools = backgrounds[index].tools
        self.equipment = backgrounds[index].equipment
        self.feature = backgrounds[index].feature
        self.num_lang = backgrounds[index].num_lang
        print("Chosen background: ", self.name)


def read_backgrounds() :
    # TODO: change to generate() function
    # TODO: instead of using local JSON, grab JSON data using API
    ''' Function to read background data from an input JSON '''
    backgrounds = []

    f = open(os.path.join(sys.path[0], "backgrounds.json"), "r")
    data = json.load(f)
    
    for elt in data["backgrounds"] :
        backgrounds.append(Background())
        backgrounds[-1].set_val(elt["name"],elt["skills"],elt["tools"],elt["equipment"],elt["languages"],elt["feature"])
    return backgrounds

sample = read_backgrounds()
