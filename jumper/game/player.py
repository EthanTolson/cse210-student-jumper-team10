

class Player:
    """A code template for the player who guesses 
    letters in a word. The responsibility of this class is to 
    hold guesses as players attempt to guess the word.

    Stereotype:
        Info Holder

    Attributes:
        i_guesses_made (list): list of letters; updates as user inputs incorrect values
        guesses_left (integer): number of guesses until player fails
        guess (character): player inputted guess
    
    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Player): An instance of Player.
        """
        self.guess = ""
        self.guesses_left = 8
        self.i_guesses_made = ["", "", "", "", "", "", "", ""]
        pass

    def get_graphic(self):
        """Returns a string that contains image to show player
        
        Args: 
            self (Player): An instance of Player.
        """

        """
          ___  
         /___\ 
         \   / 
          \ /  
           0   
          /|\  
          / \  
       
        ^^^^^^^
        """

        full_jumper = ""

        #the jumper image, and what it looks like when it is crossed out
        jumper = ["  ___  ", " /___\ ", " \   / ", "  \ /  ", "   0   ", "  /|\   ", "  / \  ", "       ", "^^^^^^^"]
        jumper_alt = ["       ", "       ", "       ", "       ", "   x   ", "  xxx   ", "  x x  ", "       ", "^^^^^^^"]

        #determine number of incorrect guesses
        i_guess_num = 0
        for i in range(len(self.i_guesses_made)):
            if self.i_guesses_made[i] != "":
                i_guess_num += 1

        #determine how many lines are crossed out (-1 because jumper list starts at 0)
        crossed_out = i_guess_num - 1 

        #concatenate full_jumper
        for i in range(len(jumper)):

            if i <= crossed_out:
                full_jumper = f"{full_jumper}\n{jumper_alt[i]}"
            else:
                full_jumper = f"{full_jumper}\n{jumper[i]}"

        #return
        return full_jumper


    def can_pick(self, s_word):
        """Returns a boolean value if the player can input the desired value
        Example: User cannot input numbers/special characters or a value 
        they have already input
        
        Args:
            self (Player): An instance of Player.
            s_word_revealed (list): a list of characters that user has correctly guessed in word
        """

        ok_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        """
        #check for speecial characters
        for i in range(len(ok_char)):
            if self.guess == ok_char[i]:
                break
            
            #if the loop has reached the end of ok_char and has not found a match with guess, return False.
            if i == len(ok_char):
                return False

        #check incorrect guesses
        for i in range(len(self.i_guesses_made)):
            if self.i_guesses_made[i] == self.guess:
                return False

        #check correct guesses
        for i in range(len(s_word)):
            if s_word[i] == self.guess:
                return False
        
        return True"""
        
        if self.guess in ok_char and self.guess not in s_word and self.guess not in self.i_guesses_made:
            return True
        else:
            return False



       
        
    def get_turns(self, valid_play):
        """Gives the number of turns remaining and updates when player uses one

        Args:
            self (Player): An instance of Player.
            valid_play (boolean): passes true if player has guessed a correct value
        """
        turns = f"You have {self.guesses_left} guesses remaining"
        if(not valid_play):
            self.guesses_left = self.guesses_left - 1

        return turns
