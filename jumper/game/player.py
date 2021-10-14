

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
        pass

    def can_pick(self, s_word):
        """Returns a boolean value if the player can input the desired value
        Example: User cannot input numbers/special characters or a value 
        they have already input
        
        Args:
            self (Player): An instance of Player.
            s_word_revealed (list): a list of characters that user has correctly guessed in word
        """
        
        pass
        
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
