import unittest


class TestTrivia(unittest.TestCase):

	import main

    #Tests opening of file, correctly
	def testCSVFormat(self):
		self.assertIsNot(myFile,null)

#	def testReadFile(self):
#		if data!= null:
#			return True


#	def testScoreDisplay(self):
#		return self.score 

  #  def testContinueGame(self):
   # 	pass

    #def testNotContinueGame(self):
    #	pass


if __name__ == '__main__':
    unittest.main()