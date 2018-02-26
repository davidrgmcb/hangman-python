from random import choice

class Word(object): #Aspects of the word itself
    def __init__(self):
        self.word = "-1" #Makes the default run afoul of the "isalpha()" call, saves a line
        self.length = len(self.word) #Just used for getting the length of the correct answer fill-in that lives in GameState. Could be just as fine outside this class I suppose but feels like a lateral move
        self.correctLetters = set() #All the correct letters that need to be guessed for comparison against the set of letters guessed
        self.listOfCorrectLetters = list(self.word) #The correct letters in a list, allows for proper display of what has been guessed correctly
        
    def fixAnswer(self): #I don't like that this exists and there's probably a better fix but not one I can quickly see
        self.listOfCorrectLetters = list(self.word)
        self.length = len(self.word)
        self.word = str.lower(self.word)
        return
        
    def randomizeAnswer(self):
        while self.word.isalpha() == False or self.length < 2: #randomizes the word so long as it hasn't already been set
            self.word = choice(possibleWords) #some of these word sources have apostrophes or nonletters in general, best to reroll if those show up
        

class GameState(object): #Aspects of the game state and how it interacts with the player
    def __init__(self):
        self.guess = "?"
        self.strikes = 0
        self.lettersGuessed = set()
        self.wordProgress = []
        self.difficulty = "1"
        
    #def guessCaseFix(self)
        