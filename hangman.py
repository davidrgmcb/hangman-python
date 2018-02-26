from random import choice
from sys import version_info
from hangmanClasses import Word, GameState
        
possibleWords = open("/usr/share/dict/words").read().split() #word randomization scheme, not exactly universally compatible at the moment but finding a freely redistributable wordlist has been harder than anticipated

answer = Word() #can't play hangman with no word to guess

game = GameState() #Necessary to immediately generate the actual gamestate

if (version_info > (3, 0)):
    game.difficulty = input("Choose your difficulty by typing 1 (Normal), 2 (Challenging), or 3 (Unfair)\n")
else:
    game.difficulty = raw_input("Choose your difficulty by typing 1 (Normal), 2 (Challenging), or 3 (Unfair)\n")
    
if (game.difficulty.isdigit()) and (int(game.difficulty) > 0) and (int(game.difficulty) < 4) and (len(game.difficulty) == 1):
    pass
else:
    print("If you want to be difficult, I'll be difficult")
    game.difficulty = "3"
    print(game.difficulty)

#while answer.word.isalpha() == False or answer.length < 2: #randomizes the word so long as it hasn't already been set
    #answer.word = choice(possibleWords) #some of these word sources have apostrophes or nonletters in general, best to reroll if those show up
    
answer.randomizeAnswer()

answer.fixAnswer()#probably a better way to do this but answer needs to be changed from its default values and have anything dependant on those "fixed", probably replace with something less stupid later

for letters in range(answer.length): #expand list into row of underscores showing how many letters remain to be guessed
    game.wordProgress.append("_")

for letter in answer.word:
    answer.correctLetters.add(letter)#makes a set of every letter in the word for easy comparison

while (game.strikes < 7) and (not answer.correctLetters.issubset(game.lettersGuessed)): #game loop executes until enough wrong guesses or all correct letters guessed

    if (version_info > (3, 0)): #A python version test, the changes to input bring the program to its knees otherwise
        game.guess = str.lower(input("Enter one letter\n")) #takes guess, ensures it isn't cased weird
    else:
        game.guess = str.lower(raw_input("Enter one letter\n")) #Ideally makes it somewhat python 2 compatible, merits careful testing

    while (len(game.guess) > 1) or (game.guess.isalpha() == False):
        print ("Please, just one letter and no numbers\n")
        if (version_info > (3, 0)): #same version compatibility attempt
            game.guess = str.lower(input("Enter one letter\n"))
        else:
            game.guess = str.lower(raw_input("Enter one letter\n"))
            
    for letter in range(0, len(answer.listOfCorrectLetters)):
        if answer.listOfCorrectLetters[letter] == game.guess:
            game.wordProgress[letter] = game.guess
        
    
    game.lettersGuessed.add(game.guess) #track what letters have been guessed, naturally
    
    if set(game.guess).issubset(answer.correctLetters): #ugly and cludgy to convert a one letter string into a set just for this, hopefully change later
        pass
    else:
        game.strikes += 1 #need penalty to be an else, probably should find a better way to put it than pass up there
        
    print(game.strikes) #Perhaps one day this morphs into an instruction to draw a hangman bit by bit and helps balloon the size of the program update: the future is now
    if game.strikes == 1:
        print("________\n|       |\n|       O")
    elif game.strikes == 2:
        print("________\n|       |\n|       O\n|       |")
    elif game.strikes == 3:
        print("________\n|       |\n|       O\n|     --|")
    elif game.strikes == 4:
        print("________\n|       |\n|       O\n|     --|--")
    elif game.strikes == 5:
        print("________\n|       |\n|       O\n|     --|--\n|      /")
    elif game.strikes == 6:
        print("________\n|       |\n|       O\n|     --|--\n|      / \\")
    elif game.strikes == 7:
        print("________\n|       |\n|       O\n|     --|--\n|      / \\ \n\n He's dead Jim")
    #crude hangman drawing, probably better solutions exist but whatever
    
    #print(answer.correctLetters) #easier to debug with a view of what's correct
    
    if int(game.difficulty) < 3: #Unfair dificulty definitely unfair
        print(' '.join(game.wordProgress)) #clean way to show what has been guessed and hint at the wrod better
    
    print("\n")
    
    print(list(game.lettersGuessed)) #frustrating to not know what you've guessed, should try to make this alphabetical later

print(game.guess)

print(answer.word)