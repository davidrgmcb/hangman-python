from random import choice
from sys import version_info

class Word(object): #Aspects of the word itself
    def __init__(self):
        self.word = "-1" #Makes the default run afoul of the "isalpha()" call, saves a line
        self.length = len(self.word) #commented out in case of use when reimplementing for more complex but aesthetically pleasing solution.
        self.correctLetters = set()
        self.correctList = list(self.word)
        
    def fixAnswer(self):
        self.correctList = list(self.word)
        self.length = len(self.word)
        return

class GameState(object): #Aspects of the game state and how it interacts with the player
    def __init__(self):
        self.guess = "?"
        self.strikes = 0
        self.lettersGuessed = set()
        self.wordProgress = []
        
possibleWords = open("/usr/share/dict/words").read().split() #word randomization schemes,this one along with limited UI makes this mindnumbingly hard, maybe make this a hard mode and find an easier list

answer = Word() #can't play hangman with no word to guess

game = GameState() #Necessary to immediately generate the actual gamestate

while answer.word.isalpha() == False: #randomizes the word so long as it hasn't already been set
    answer.word = choice(possibleWords) #some of these word sources have apostrophes or nonletters in general, best to reroll if those show up

answer.fixAnswer()#probably a better way to do this but answer needs to be changed from its default values and have anything dependant on those "fixed", probably replace with something less stupid later

answer.word = str.lower(answer.word) #makes sure the word stays standardized to lower case regardless of source

for letters in range(answer.length): #expand list into row of underscores showing how many letters remain to be guessed
    game.wordProgress.append("_")
    print (game.wordProgress)

for letter in answer.word:
    answer.correctLetters.add(letter)#makes a set of every letter in the word for easy comparison

while (game.strikes < 7) and (not answer.correctLetters.issubset(game.lettersGuessed)): #game loop executes until enough wrong guesses or all correct letters guessed

    if (version_info > (3, 0)): #A python version test, the changes to input bring the program to its knees otherwise
        game.guess = str.lower(input("Enter one letter\n")) #takes guess, ensures it isn't cased weird
    else:
        game.guess = str.lower(raw_input("Enter one letter\n")) #Ideally makes it somewhat python 2 compatible, merits careful testing

    while (len(game.guess) > 1) or (game.guess.isalpha() == False):
        if (version_info > (3, 0)): #same version compatibility attempt
            print ("Please, just one letter and no numbers\n")
            game.guess = str.lower(input("Enter one letter\n"))
        else:
            print ("Please, just one letter and no numbers\n")
            game.guess = str.lower(raw_input("Enter one letter\n"))
            
    for letter in answer.correctList:
        if answer.correctList == game.guess:
            game.wordProgress[letter] = game.guess
            print(game.wordProgress)
        
    
    game.lettersGuessed.add(game.guess) #track what letters have been guessed, naturaly
    
    if set(game.guess).issubset(answer.correctLetters): #ugly and cludgy to convert a one letter string into a set just for this, hopefully change later
        pass
    else:
        game.strikes += 1 #need penalty to be an else, probably should find a better way to put it than pass up there
        
    print(game.strikes) #Perhaps one day this morphs into an instruction to draw a hangman bit by bit and helps balloon the size of the program
    
    print(answer.correctLetters) #easier to debug with a view of what's correct
    
    print(' '.join(game.wordProgress)) #clean way of showing that
    
    #print(answer.correctList)
    
    print(game.lettersGuessed) #frustrating to not know what you've guessed, should try to make this alphabetical later

print(game.guess)

print(answer.word)

#Work on display, of letters in word correctly guessed, of hangman. Aesthetics time.