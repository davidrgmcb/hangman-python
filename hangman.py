from hangmanClasses import Word, GameState


answer = Word() #can't play hangman with no word to guess

game = GameState() #Necessary to immediately generate the actual gamestate

game.getDifficultySelection() #prompts for and sets a valid difficulty, responds with hostility if an invalid difficulty is chosen
    
answer.randomizeAnswer() #sets a random word to be the answer that ends the game on being fully guessed

answer.fixAnswer() #rename this, currently sets the word.word attribute, enforces lowercase on the answer, sets the propere length and sets the ordered list of correct letters

game.createWordProgressIndicator(answer) #makes the list of underscores used in display later, takes in answer to know what that length should be

answer.getCorrectLetterComparisonSet() #gets a set of every letter contained in the word

while (game.strikes < 7) and (not answer.correctLetters.issubset(game.lettersGuessed)): #game loop executes until enough wrong guesses or all correct letters guessed

    game.guessEnforceLowerCase() #Ensures that the guess entered is lowercase regardless of whether it was entered as a capital letter or not
            
    game.updateCorrectLetterDisplay(answer) #updates the line of underscores matching the length of the correct guess, replacing underscores with correctly guessed letters
        
    game.addCurrentGuessToGuessedSet() #track what letters have been guessed, naturally
        
    game.checkGuess(answer) #checks if the guess was correct, adds to game.strikes if it isn't
        
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
    elif game.strikes >= 7:
        print("________\n|       |\n|       O\n|     --|--\n|      / \\ \n\n He's dead Jim")
    #crude hangman drawing, probably better solutions exist but whatever
    
    #print(answer.correctLetters) #easier to debug with a view of what's correct
    
    if int(game.difficulty) < 3: #Unfair dificulty definitely unfair
        print(' '.join(game.wordProgress)) #clean way to show what has been guessed and hint at the word better
    
    print("\n")
    
    print(list(game.lettersGuessed)) #frustrating to not know what you've guessed, should try to make this alphabetical later

print(game.guess)

print(answer.word)