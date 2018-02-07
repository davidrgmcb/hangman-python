#import sys
import random

class Word(object): #Aspects of the word itself
    def __init__(self):
        self.word = "unpopulated"
        #self.length = len(self.word) commented out in case of use when reimplementing for more complex but aesthetically pleasing solution.
        self.correctLetters = set()

class GameState(object): #Aspects of the game state and how it interacts witht he player
    def __init__(self):
        self.guess = "?"
        self.strikes = 0
        self.lettersGuessed = set()
        
possibleWords = ["test", "nurtures", "paranoia", "mellow", "populated"] #sample list of words for testing random generation setup

game = GameState() #Necessary to immediately generate the actual gamestate

answer = Word() #can't play hangman with no word to guess

answer.word = random.choice(possibleWords) #would get pretty boring if you couldn't have multiple words, method of randomly getting words subject to change

for i in answer.word:
    answer.correctLetters.add(i)#makes a set of every letter int he word for easy comparison

while (game.strikes < 7) and (not answer.correctLetters.issubset(game.lettersGuessed)): #game loop executes until enough wrong guesses or all correct letters guessed

    game.guess = input("Enter one letter\n")

    while len(game.guess) > 1:
        print ("Please, just one letter\n")
        game.guess = input("Enter one letter\n")
    
    game.lettersGuessed.add(game.guess)
    
    if set(game.guess).issubset(answer.correctLetters):
        pass
    else:
        game.strikes += 1
        
    print(game.strikes)

print(game.guess)

print(answer.word)

print(game.lettersGuessed)