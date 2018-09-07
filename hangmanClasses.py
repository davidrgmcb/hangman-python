from random import choice
from sys import version_info

class Word(object): #Aspects of the word itself
    def __init__(self):
        self.possibleWords = open("/usr/share/dict/words").read().split() #word randomization scheme, not exactly universally compatible at the moment but finding a freely redistributable wordlist has been harder than anticipated
        self.word = str.lower(choice(self.possibleWords))
        while self.word.isalpha() == False or len(self.word) < 2: #randomizes the word so long as it hasn't already been set
            self.word = str.lower(choice(self.possibleWords)) #some of these word sources have apostrophes or nonletters in general, best to reroll if those show up
        self.correctLetters = set(self.word) #All the correct letters that need to be guessed for comparison against the set of letters guessed
        self.listOfCorrectLetters = list(self.word) #The correct letters in a list, allows for proper display of what has been guessed correctly
            
    def endOfGameReveal(self, GameState):
        if (GameState.strikes >=7): #In retrospect I'm not sure why this conditional check is here, consider removing.
            print(self.word)
            
    def newWord(self):
        self.word = str.lower(choice(self.possibleWords))
        while self.word.isalpha() == False or len(self.word) < 2: #randomizes the word so long as it hasn't already been set
            self.word = str.lower(choice(self.possibleWords)) #some of these word sources have apostrophes or nonletters in general, best to reroll if those show up
        self.correctLetters = set(self.word) #All the correct letters that need to be guessed for comparison against the set of letters guessed
        self.listOfCorrectLetters = list(self.word) #The correct letters in a list, allows for proper display of what has been guessed correctly
        

class GameState(object): #Aspects of the game state and how it interacts with the player
    def __init__(self):
        self.guess = "?"
        self.strikes = 0
        self.lettersGuessed = set()
        self.wordProgress = []
        self.difficulty = "1"
        self.willReplay = True
        self.playRepeat = "N"
        
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
            print("Difficulty is now {} (Unfair)".format(self.difficulty))
            
    def createWordProgressIndicator(self, Word):
        for letters in range(len(Word.word)): #expand list into row of underscores showing how many letters remain to be guessed
            self.wordProgress.append("_")
        
    def getGuess(self):
        if (version_info > (3, 0)): #A python version test, the changes to input bring the program to its knees otherwise
            self.guess = str.lower(input("Enter one letter\n")) #takes guess, ensures it isn't cased weird
        else:
            self.guess = str.lower(raw_input("Enter one letter\n")) #Ideally makes it somewhat python 2 compatible, merits careful testing
#maybe split these
        while (len(self.guess) > 1) or (self.guess.isalpha() == False):
             print ("Please, just one letter and no numbers or symbols\n")
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
        if int(self.difficulty) == 1 and self.guess not in (Word.correctLetters): #Looks a little cleaner to me than arbitrary set conversion or calling __contains__ directly
            self.strikes += 1
        elif int(self.difficulty) > 1 and self.guess not in (Word.correctLetters):
            self.strikes += 2 #Finally found a place to sneak in a distinction between difficulty 2 and 3, nearly entirely luck based now but hey this is a coding exercise not a game design exercise
            
    def printHangman(self):
        print(self.strikes) #A little superfluous now, but I don't think it muddies up the presentation and it can be nice to have an idea of how close you are to failure
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
    
    def playAgain(self, Word): #text prompting whether to reset the game state and play again, takes in Word so it can pass it to resetGame if that is called, inelegant but oh well.
        if (version_info > (3, 0)):
            self.playRepeat = input("Would you like to play again? Y for yes N for no\n")
            self.playRepeat = self.playRepeat.upper() #Just standardize the case
            print(self.playRepeat)
            if (self.playRepeat == "Y"):
                self.resetGame(Word)
            else:
                print("Okay, thanks for playing!\n")
                self.willReplay = False
                pass
        else:
            self.playRepeat = raw_input("Would you like to play again? Y for yes N for no\n")
            self.playRepeat = self.playRepeat.upper()
            print(self.playRepeat)
            if (self.playRepeat == "Y"):
                self.resetGame(Word)
            else:
                print("Okay, thanks for playing!\n")
                self.willReplay = False
                pass
            
    
    def resetGame(self, Word): #should set everything back to scratch enough to play again
        Word.newWord() #Essentially reinits but just reuses the already loaded dictionary
        self.guess = "?"
        self.strikes = 0
        self.lettersGuessed.clear() #Not much different than just pointing it to an empty set, but theoretically a very slight memory save, not that it matters in this context.
        del self.wordProgress[:] #Same
        self.difficulty = "1" #Player might want to play on a different difficulty, this is probably unnecessary though
        self.getDifficultySelection()
        self.createWordProgressIndicator(Word)