#import sys
import random

class Word(object): #Aspects of the word itself
    def __init__(self):
        self.word = "unpopulated"
        self.length = len(self.word)

class GameState(object): #Aspects of the game state and how it interacts witht he player
    def __init__(self):
        self.guess = "?"
        self.strikes = 0
        #self.numberOfCurrentLetters = 0 replace
        
possibleWords = ["paranoia", "nurtures", "him", "mellow", "populated"] #sample list of words for testing random generation setup

game = GameState()

answer = Word()

answer.word = random.choice(possibleWords)

if game.guess == "?":
    game.guess = input("Enter one letter\n")

while len(game.guess) > 1:
    print ("Please, just one letter\n")
    game.guess = input("Enter one letter\n")

print(game.guess)

print(answer.word)

#guess = str(guess)

#if __name__ == '__main__':
 #   main()