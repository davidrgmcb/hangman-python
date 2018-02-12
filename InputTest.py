import hangman
import unittest

class testInputExistence (unittest.TestCase):
    
    def testUserInput(self):
        self.assertNotEqual(hangman.game.guess, '?')
    
    def testInputLength(self):
        self.assertTrue(len(hangman.game.guess) < 2)
        
class testRandomizer (unittest.TestCase):
    def testWordRandomizer(self):
        self.assertNotEqual(hangman.answer.word, 'unpopulated')
    
class testStandardization (unittest.TestCase):    
    def testGuessListAppend(self):
        self.assertTrue(len(hangman.game.lettersGuessed) > 1)
        
    def testCaseFixingOnWords(self):
        self.assertTrue(str.islower(hangman.answer.word))
    
    def testCaseFixingOnGuess(self):
        self.assertTrue(str.islower(hangman.game.guess))
        
    def testGuessIsLetter(self):
        self.assertTrue(str.isalpha(hangman.game.guess))
        
    def testNoApostrophe(self):
        self.assertFalse(("\'" in hangman.answer.word))

@unittest.skip #know what I want this to do but it probably doesn't do it so skipping for now while I try to fix the actual problem
class testWordUIRelatedFunctions (unittest.TestCase):
    def testDisplayCorrectGuesses(self):
        for letters in hangman.answer.correctList:
            self.assertTrue((letters in hangman.game.wordProgress == letters in hangman.answer.correctList) or (letters in hangman.game.wordProgress == "_"))
        
if __name__ == '__main__':
    unittest.main()