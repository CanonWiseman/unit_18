import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    
    def __init__(self, file_path):
        self.file = open(file_path, "r")
        self.lines = self.file.readlines()
       
        print(f"{len(self.lines)} words read")

    def random(self):
        rand_word = random.choice(self.lines)
        return rand_word.strip("\n")

        
class SpecialWordFinder(WordFinder):

    def __init__(self, file_path):
        
        super().__init__(file_path)
    

    def random(self):

        found = False

        while found == False:
            rand_word = random.choice(self.lines)
            if not rand_word[0] == "#" and not rand_word.strip("\n") == '':
                return rand_word.strip("\n")

            




