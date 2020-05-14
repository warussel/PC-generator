# Background class for character backgrounds
import json
import os
import sys

class Background :
    ''' A class representing a character's background '''

    # TODO: remove input from this function. __init__ should use default values
    def __init__(self,name_in,skills_in,tools_in,equip_in,lang_in,feature_in) :
        self.name = name_in
        self.skills = skills_in
        self.tools = tools_in
        self.equipment = equip_in
        self.feature = feature_in
        self.num_lang = lang_in

def read_backgrounds() :
    # TODO: change to generate() function
    # TODO: instead of using local JSON, grab JSON data using API
    ''' Function to read background data from an input JSON '''
    backgrounds = []

    f = open(os.path.join(sys.path[0], "backgrounds.json"), "r")
    data = json.load(f)
    
    for elt in data["backgrounds"] :
        backgrounds.append(Background(elt["name"],elt["skills"],elt["tools"],elt["equipment"],elt["languages"],elt["feature"]))
        backgrounds.
        print("Added: ", elt["name"])
    return backgrounds

sample = read_backgrounds()
