from game.player import Player
from game.console import Console
from game.secretword import Secretword as SW

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        player (Player): An instance of the class of objects known as Player.
        s_word (Secretword): An instance of the class of objects known as Secretword.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.player = Player()
        self.keep_playing = True
        self.s_word = SW()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """

        pass

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,

        Args:
            self (Director): An instance of Director.
        """
        pass

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case,

        Args:
            self (Director): An instance of Director.
        """
        pass

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case,

        Args:
            self (Director): An instance of Director.
        """
        pass