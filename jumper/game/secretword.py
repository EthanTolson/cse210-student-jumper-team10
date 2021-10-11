import random

class Secretword:
    def __init__(self):


        self.s_word = "ERROR"

        with open("jumper/game/wordss.txt", "r") as file:
            words = file.readlines()
            self.s_word = words[random.randint(0,9509)]

        self.s_word = self.s_word.strip()
        if(self.s_word == "ERROR"):
            print("There is an issue with the program. Program should still run properly. ERROR with file.")
        print(f"Secret Word has been chosen! (¬‿ ¬) {self.s_word}")


        
        pass