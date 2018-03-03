from hangmanClasses import Word, GameState


answer = Word() #can't play hangman with no word to guess

game = GameState() #Necessary to immediately generate the actual gamestate

game.getDifficultySelection() #prompts for and sets a valid difficulty, responds with hostility if an invalid difficulty is chosen

game.createWordProgressIndicator(answer) #makes the list of underscores used in display later, takes in answer to know what that length should be

while (game.strikes < 7) and (not answer.correctLetters.issubset(game.lettersGuessed)): #game loop executes until enough wrong guesses or all correct letters guessed

    game.getGuess() #Ensures that the guess entered is lowercase regardless of whether it was entered as a capital letter or not
            
    game.updateCorrectLetterDisplay(answer) #updates the line of underscores matching the length of the correct guess, replacing underscores with correctly guessed letters
        
    game.addCurrentGuessToGuessedSet() #track what letters have been guessed, naturally
        
    game.checkGuess(answer) #checks if the guess was correct, adds to game.strikes if it isn't
        
    game.printHangman() #Prints a small hangman ascii based on how high game.strikes is
    
    #print(answer.correctLetters) #easier to debug with a view of what's correct
    
    game.showProgress() #prints the list of underscores and corectly guessed letters
    
    game.showGuesses() #prints an alphabetical list of all the guessed letters

answer.endOfGameReveal(game)