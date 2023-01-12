class Words:
   def getString(self):
      self.string = input()
   def printString(self):
      print(self.string.upper())

word = Words()
word.getString()
word.printString()
