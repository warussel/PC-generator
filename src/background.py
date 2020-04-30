# Background class for character backgrounds
import json
import os
import sys

class Background :
    ''' A class representing a character's background '''

    def __init__(self) :
        skills = []
        tools = []
        equipment = []
        feature = ""
        print("TODO: implement me!")

def read_backgrounds() :
    ''' Read background data from an input JSON '''
    backgrounds = []

    f = open(os.path.join(sys.path[0], "backgrounds.json"), "r")
    data = json.load(f)
    
    print("Printing backgrounds: ")
    for elt in data["backgrounds"] :
        # TODO: Add backgrounds to array
        print(elt["name"])

read_backgrounds()