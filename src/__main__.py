# Main class to run generator script
import random
from character import Character

def main():
    ''' Main function to generate a simple character '''
        
    # Build Character
    name = "Yin" # TODO: Input character name
    PC = Character(name)
    PC.generate()

if __name__ == "__main__":
    main()
