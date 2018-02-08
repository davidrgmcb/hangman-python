import random

class Word(object): #Aspects of the word itself
    def __init__(self):
        self.word = "unpopulated"
        #self.length = len(self.word) commented out in case of use when reimplementing for more complex but aesthetically pleasing solution.
        self.correctLetters = set()

class GameState(object): #Aspects of the game state and how it interacts with the player
    def __init__(self):
        self.guess = "?"
        self.strikes = 0
        self.lettersGuessed = set()
        
#possibleWords = ["test", "nurtures", "paranoia", "mellow", "populated"] 
possibleWords = open("/usr/share/dict/words").read().split() #word randomization schemes

game = GameState() #Necessary to immediately generate the actual gamestate

answer = Word() #can't play hangman with no word to guess

answer.word = random.choice(possibleWords) #would get pretty boring if you couldn't have multiple words, method of randomly getting words subject to change

while "\'" in answer.word:
    answer.word = random.choice(possibleWords) #some of these word sources have apostrophes, best to reroll if those show up

answer.word = str.lower(answer.word) #makes sure the word stays standardized to lower case regardless of source

for i in answer.word:
    answer.correctLetters.add(i)#makes a set of every letter int he word for easy comparison

while (game.strikes < 7) and (not answer.correctLetters.issubset(game.lettersGuessed)): #game loop executes until enough wrong guesses or all correct letters guessed

    game.guess = str.lower(input("Enter one letter\n")) #takes guess, ensures it isn't cased weird

    while len(game.guess) > 1:
        print ("Please, just one letter\n")
        game.guess = str.lower(input("Enter one letter\n"))
        
    while game.guess.isalpha() == False:
        print("Letters only please\n")
        game.guess = str.lower(input("Enter one letter\n")) #lot of essentially repeat lines here, hope to fix that but who knows if it'd just make it harder to read
    
    game.lettersGuessed.add(game.guess) #track what letters have been guessed, naturaly
    
    if set(game.guess).issubset(answer.correctLetters): #ugly and cludgy to convert a one letter string into a set just for this, hopefully change later
        pass
    else:
        game.strikes += 1 #need penalty to be an else, probably should find a better way to put it than pass up there
        
    print(game.strikes) #Perhaps one day this morphs into an instruction to draw a hangman bit by bit and helps balloon the size of the program
    
    print(game.lettersGuessed) #frustrating to not know what you've guessed, should try to make this alphabetical later

print(game.guess)

print(answer.word)