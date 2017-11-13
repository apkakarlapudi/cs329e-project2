import unittest
import main

class TestTrivia(unittest.TestCase):

	#Tests set up of file
	def setUp(self):
		self.testdata = open("main.py").read()

	#Tests opening of file, correctly
	def testOpenFile(self):
		myFile = open("trivia.csv","r")
		self.assertFalse(type(myFile) is str)

	#Test whether the score is an integer or not before playing the game
	def testScoreDisplay(self):
		score = 0
		self.assertTrue(type(score) is int)

if __name__ == '__main__':
	unittest.main()
