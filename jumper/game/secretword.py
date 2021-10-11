import random

class Secretword:
    def __init__(self):


        self.s_word = ""
        with open("jumper/game/wordss.txt", "r") as file:
            words = file.readlines()
            self.s_word = words[random.randint(0,9509)]
        self.s_word = self.s_word.strip()
        print(f"Secret Word has been chosen! (¬‿ ¬) {self.s_word}")


        
        pass