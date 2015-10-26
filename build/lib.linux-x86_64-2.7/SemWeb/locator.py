import sqlite3, bintrees, os

class locator():
	
	def __init__(self,location):
		self.location = location
		self.rbt = bintrees.RBTree()

	def __createTree(self):
		myFiles = os.listdir(self.location)
		for f in myFiles:
			if self.location[len(self.location)-1] =="/":
				currentLocation = self.location + f
			else:
				currentLocation = self.location + "/"+f
			if(os.path.isfile(currentLocation)==True):
				self.rbt.insert(f, currentLocation)
	
	def findLocation(self, name):
		self.__createTree()
		location = self.rbt.get(name)
		return location

