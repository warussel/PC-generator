# Main class to run generator script

import random
from character import Character

# --------- NOTE: THIS SCRIPT HAS BEEN REPLACED WITH APP.PY -----------
# --------------- ONLY USE THIS SCRIPT FOR TESTING PURPOSES -----------
def main():
    ''' Main function to generate a simple character '''
        
    # Build Character
    name = "Yin" # TODO: Input character name
    PC = Character(name)
    PC.generate("","","")

if __name__ == "__main__":
    main()
