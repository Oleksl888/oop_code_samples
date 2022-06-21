"""Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A).
This class is going to represent a human player. In addition to having all of the instance variables and
methods that WOFPlayer has, WOFHumanPlayer should have an additional method:
    .getMove(category, obscuredPhrase, guessed): Should ask the user to enter a move (using input())
    and return whatever string they entered.
The user can then enter:
    'exit' to exit the game
    'pass' to skip their turn
    a single character to guess that letter
    a complete phrase (a multi-character phrase other than 'exit' or 'pass') to guess that phrase
Note that .getMove() does not need to enforce anything about the user’s input; that will be done via the game
logic that we define in the next ActiveCode window.
"""
from part1 import WOFPlayer


class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        line = input(f'''{self.name} has ${self.prizeMoney}

Category: {category}
Phrase:  {obscuredPhrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':''')
        return line
