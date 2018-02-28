from random import choice
from sys import version_info

class Word(object): #Aspects of the word itself
    def __init__(self):
        self.word = "-1" #Makes the default run afoul of the "isalpha()" call, saves a line
        self.length = len(self.word) #Just used for getting the length of the correct answer fill-in that lives in GameState. Could be just as fine outside this class I suppose but feels like a lateral move
        self.correctLetters = set() #All the correct letters that need to be guessed for comparison against the set of letters guessed
        self.listOfCorrectLetters = list(self.word) #The correct letters in a list, allows for proper display of what has been guessed correctly
        self.possibleWords = open("/usr/share/dict/words").read().split() #word randomization scheme, not exactly universally compatible at the moment but finding a freely redistributable wordlist has been harder than anticipated
        
    def fixAnswer(self): #I don't like that this exists and there's probably a better fix but not one I can quickly see
        self.listOfCorrectLetters = list(self.word)
        self.length = len(self.word)
        self.word = str.lower(self.word)
        return
        
    def randomizeAnswer(self):
        while self.word.isalpha() == False or self.length < 2: #randomizes the word so long as it hasn't already been set
            self.word = choice(self.possibleWords) #some of these word sources have apostrophes or nonletters in general, best to reroll if those show up
            
    def getCorrectLetterComparisonSet(self):
        for letter in self.word:
            self.correctLetters.add(letter)#makes a set of every letter in the word for easy comparison
            
    def endOfGameReveal(self, GameState):
        if (GameState.strikes >=7):
            print(self.word)
        

class GameState(object): #Aspects of the game state and how it interacts with the player
    def __init__(self):
        self.guess = "?"
        self.strikes = 0
        self.lettersGuessed = set()
        self.wordProgress = []
        self.difficulty = "1"
        
    def getDifficultySelection(self):
        if (version_info > (3, 0)):
            self.difficulty = input("Choose your difficulty by typing 1 (Normal), 2 (Challenging), or 3 (Unfair)\n")
        else:
            self.difficulty = raw_input("Choose your difficulty by typing 1 (Normal), 2 (Challenging), or 3 (Unfair)\n")
        
        if (self.difficulty.isdigit()) and (int(self.difficulty) > 0) and (int(self.difficulty) < 4) and (len(self.difficulty) == 1):
            pass
        else:
            self.difficultyInvalidMessage()
        
        
    def difficultyInvalidMessage(self):
            print("If you want to be difficult, I'll be difficult")
            self.difficulty = "3"
            print(self.difficulty)
            
    def createWordProgressIndicator(self, Word):
        for letters in range(Word.length): #expand list into row of underscores showing how many letters remain to be guessed
            self.wordProgress.append("_")
        
    def guessEnforceLowerCase(self):
        if (version_info > (3, 0)): #A python version test, the changes to input bring the program to its knees otherwise
            self.guess = str.lower(input("Enter one letter\n")) #takes guess, ensures it isn't cased weird
        else:
            self.guess = str.lower(raw_input("Enter one letter\n")) #Ideally makes it somewhat python 2 compatible, merits careful testing

        while (len(self.guess) > 1) or (self.guess.isalpha() == False):
             print ("Please, just one letter and no numbers\n")
             if (version_info > (3, 0)): #same version compatibility attempt
                 self.guess = str.lower(input("Enter one letter\n"))
             else:
                 self.guess = str.lower(raw_input("Enter one letter\n"))
                 
    def updateCorrectLetterDisplay(self, Word):
        for letter in range(0, len(Word.listOfCorrectLetters)):
            if Word.listOfCorrectLetters[letter] == self.guess:
                self.wordProgress[letter] = self.guess
                
    def addCurrentGuessToGuessedSet(self):
        self.lettersGuessed.add(self.guess) #track what letters have been guessed, naturally
        
    def checkGuess(self, Word):
        if set(self.guess).issubset(Word.correctLetters): #ugly and cludgy to convert a one letter string into a set just for this, hopefully change later
            pass
        else:
            self.strikes += 1 #need penalty to be an else, probably should find a better way to put it than pass up there
            
    def printHangman(self):
        print(self.strikes) #Perhaps one day this morphs into an instruction to draw a hangman bit by bit and helps balloon the size of the program update: the future is now
        if self.strikes == 1:
            print("________\n|       |\n|       O")
        elif self.strikes == 2:
            print("________\n|       |\n|       O\n|       |")
        elif self.strikes == 3:
            print("________\n|       |\n|       O\n|     --|")
        elif self.strikes == 4:
            print("________\n|       |\n|       O\n|     --|--")
        elif self.strikes == 5:
            print("________\n|       |\n|       O\n|     --|--\n|      /")
        elif self.strikes == 6:
            print("________\n|       |\n|       O\n|     --|--\n|      / \\")
        elif self.strikes >= 7:
            print("________\n|       |\n|       O\n|     --|--\n|      / \\ \n\n He's dead Jim")
            
    def showProgress(self):
        if int(self.difficulty) < 3: #Unfair dificulty definitely unfair
             print(' '.join(self.wordProgress)) #clean way to show what has been guessed and hint at the word better
             
    def showGuesses(self):
        print("\n")
        print(sorted(list(self.lettersGuessed))) #frustrating to not know what you've guessed
        
    def reprintGuess(self):
        print(self.guess)