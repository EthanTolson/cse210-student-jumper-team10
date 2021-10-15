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
        while self.keep_playing:
            
            self.get_inputs()
            self.do_outputs()
            self.do_updates()
            

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case, gets user character.

        Args:
            self (Director): An instance of Director.
        """

        valid = False
        while valid == False:
            self.player.guess = self.console.read("Guess a letter a-z: ") 
            if self.player.can_pick(self.s_word.s_word_revealed):
                valid = True

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, updates whether the player can continue to play

        Args:
            self (Director): An instance of Director.
        """
        
        if self.player.guesses_left <= 0 or "_" not in self.s_word.s_word_revealed:
            self.keep_playing = False

        if self.player.guess not in self.s_word.s_word_revealed:
            self.player.i_guesses_made.append(self.player.guess)

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, outputs the graphic, correctly guessed letters and nuber of turns left.

        Args:
            self (Director): An instance of Director.
        """
        self.console.write(self.player.get_turns(self.s_word.check_guess(self.player.guess)))
        self.console.write(self.s_word.secret_word_revealer())
        self.console.write(self.player.get_graphic())
        
        