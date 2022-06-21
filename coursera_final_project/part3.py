'''Finally, we’re going to define a class named WOFComputerPlayer, which should inherit from WOFPlayer (part A).
This class is going to represent a computer player.
Every computer player will have a difficulty instance variable. Players with a higher difficulty generally play “better”.
There are many ways to implement this. We’ll do the following:
    If there aren’t any possible letters to choose (for example: if the last character is a vowel but this player
    doesn’t have enough to guess a vowel), we’ll 'pass'
    Otherwise, semi-randomly decide whether to make a “good” move or a “bad” move on a given turn (a higher difficulty
    should make it more likely for the player to make a “good” move)
            To make a “bad” move, we’ll randomly decide on a possible letter.
            To make a “good” move, we’ll choose a letter according to their overall frequency in the English language.
In addition to having all of the instance variables and methods that WOFPlayer has, WOFComputerPlayer should have:
Class variable
    .SORTED_FREQUENCIES: Should be set to 'ZQXJKVBPYGFWMUCLDRHSNIOATE', which is a list of English characters sorted
     from least frequent ('Z') to most frequent ('E'). We’ll use this when trying to make a “good” move.
Additional Instance variable
    .difficulty: The level of difficulty for this computer (should be passed as the second argument into the constructor after .name)
Methods
    .smartCoinFlip(): This method will help us decide semi-randomly whether to make a “good” or “bad” move. A higher
     difficulty should make us more likely to make a “good” move. Implement this by choosing a random number
      between 1 and 10 using random.randint(1, 10) (see above) and returning False if that random number is greater
      than self.difficulty. If the random number is less than or equal to self.difficulty, return True.
    .getPossibleLetters(guessed): This method should return a list of letters that can be guessed.
            These should be characters that are in LETTERS ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') but not in the guessed parameter.
            Additionally, if this player doesn’t have enough prize money to guess a vowel (variable VOWEL_COST set to 250),
            then vowels (variable VOWELS set to 'AEIOU') should not be included
    .getMove(category, obscuredPhrase, guessed): Should return a valid move.
            Use the .getPossibleLetters(guessed) method described above.
            If there aren’t any letters that can be guessed (this can happen if the only letters left to guess are vowels
            and the player doesn’t have enough for vowels), return 'pass'
            Use the .smartCoinFlip() method to decide whether to make a “good” or a “bad” move
                    If making a “good” move (.smartCoinFlip() returns True), then return the most frequent
                    (highest index in .SORTED_FREQUENCIES) possible character
                    If making a “bad” move (.smartCoinFlip() returns False), then return a random character from the
                    set of possible characters (use random.choice())
'''
from part1 import WOFPlayer
from part2 import WOFHumanPlayer
from random import randint, choice

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS  = 'AEIOU'
VOWEL_COST  = 250
guessed = ['Z', 'X', 'K', 'F', 'U', 'E', 'T']

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        super().__init__(name)
        #WOFPlayer.__init__(self, name) inititalizing name from super class WOFPLAYER
        self.difficulty = difficulty

    def smartCoinFlip(self):
        num = randint(1, 10)
        return True if num <= self.difficulty else False

    def getPossibleLetters(self, guessed):
        if self.prizeMoney >= VOWEL_COST:
            return list(set(LETTERS) - set(guessed))
        else:
            letters = set(LETTERS) - set(VOWELS)
            return list(set(letters) - set(guessed))

    def getMove(self, category, obscuredPhrase, guessed):
        print(f'''{self.name} has ${self.prizeMoney}

Category: {category}
Phrase:  {obscuredPhrase}
Guessed: {guessed}

Guess a letter, phrase, or type 'exit' or 'pass':''')
        if self.smartCoinFlip():
            for char in reversed(self.SORTED_FREQUENCIES):
                if char in self.getPossibleLetters(guessed):
                    return char
            return 'pass'
        else:
            if not choice(self.getPossibleLetters(guessed)):
                pass
            else:
                return choice(self.getPossibleLetters(guessed))


me = WOFComputerPlayer('Aex', 7)
print(me.name)
print(me.difficulty)
print(me.smartCoinFlip())
print(me.getPossibleLetters(guessed))
me.addMoney(500)
print(me.getPossibleLetters(guessed))
print(me.prizeMoney)
print(me.getMove("1", '2', guessed))