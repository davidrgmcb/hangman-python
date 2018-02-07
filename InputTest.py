import hangman
import unittest

class testInputExistence (unittest.TestCase):
    
    def testUserInput(self):
        self.assertNotEqual(hangman.game.guess, '?')
    
    def testInputLength(self):
        self.assertTrue(len(hangman.game.guess) < 2)
        
    def testWordRandomizer(self):
        self.assertNotEqual(hangman.answer.word, 'unpopulated')
        
    def testGuessListAppend(self):
        self.assertTrue(len(hangman.game.lettersGuessed) > 1)
        
if __name__ == '__main__':
    unittest.main()