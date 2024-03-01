"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """read the file and find random words from it"""
    def __init__(self, path):
        """open & read the file then return words read"""

        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def  parse(self, file):
        """parse file and return words"""

        return [w.strip() for w in file]

    # why cannot use: (can return it directly from word list?)
    #   def  parse(self):
    #    """parse file and return words"""

    #    return [w.strip() for w in self.words]

    def random(self):
        """return a random word"""

        return random.choice(self.words)
    
    # do i need to cloase the file after read? if yes, where should i put closing code?


    class SpecialWorldFinder(WordFinder):
        """based on WordFinder, skip the blanks and comments"""

        def parse(self, file):

            return [w.strip() for w in file 
                    if w.strip() and not w.startswith('#')]
    

    
