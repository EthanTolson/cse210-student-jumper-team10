import random
import os

class Secretword:
    """A code template for the secret word that the 
    computer chooses for each game. The responsibility 
    of this class is to get a secret word for the user to guess.
    
    Stereotype:
        Info Holder

    Attributes:
        s.word (list): list of letters that make up secret word
        s_word_revealed (list): list of charaters that make 
            up non guessed and guessed letters of secret word
    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Secretword): an instance of Secretword
        """

        self.s_word = "ER"
        self.correct_guess = []
        cwd = os.getcwd().replace("\\","/")

        with open(f"{cwd}/cse210-student-jumper-team10/jumper/game/wordss.txt", "r") as file:
            words = file.readlines()
            self.s_word = words[random.randint(0,9509)]

        self.s_word = self.s_word.strip()
        if(self.s_word == "ER"):
            print("There is an issue with the program. Program should still run properly. ERROR with file.")
        print(f"Secret Word has been chosen! (¬‿ ¬)\n")
        self.s_word_revealed = []
        for value in self.s_word:
            self.s_word_revealed.append("_")
        
        

    def check_guess(self, guess):
        """Returns true if guess is in secret word and updates s_word_reavealed
        Args:
            self (Secretword): an instance of Secretword
            guess (charater): user inputted guess
        """
        for i in range(0,len(self.s_word)):
            if guess == self.s_word[i]:
                self.s_word_revealed[i] = self.s_word[i].upper()
            
        if guess in self.s_word:
            return True
        else:
            return False

        """self.correct_guess = []
        self.correct_guess.append(self.s_word.find(guess))
        while(self.correct_guess[-1] != -1):
           self.correct_guess.append(self.s_word.find(guess, self.correct_guess[-1]))
        if(self.correct_guess[-1] == -1):
            self.correct_guess.pop()"""

    def secret_word_revealer(self):
        """Returns a message with the correct guesses revealed. 
        
        Ex.        _ _ A _ _
        
        Args:
            self
        """
        message = ""
        for i in range(0, len(self.s_word_revealed)):
            message = message + f"{self.s_word_revealed[i]} "
        
        return message