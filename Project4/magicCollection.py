#Andrew Shelton
#python 2.7
class collection:
	def __init__(self):
		self.collection = []	#list of cards in collection
	def __repr__(self):
		output = ""
		for card in self.collection:
			output= output+card.out()
		return output
	def addCard(self, card):
		#returns nothing just adds the card obj to the collection
		self.collection.append(card)

	def findCard(self, string):
		#prints the card if in the collection
		for card in self.collection:
			if card.isCard(string):
				return card
			else:
				pass
		return None

	def findCards(self, substring):
		cardList = []
		for card in self.collection:
			if card.isInCard(substring):
				cardList.append(card)
			else:
				pass

		if len(cardList)>0:
			return cardList
		else:
			return cardList
			
	def readFile(self,filename):
		with open (filename, 'r') as f:
			for line in f:
				x = line.strip('\n')
				x = x.split(" ||| ")
				temp = card(x[0],x[1],x[2])
				self.addCard(temp)

	def writeFile(self,filename):
		filename = filename
		with open (filename, 'w') as f:
			for card in self.collection:
				f.write(card.out())

	def enterCards(self):
		print "If you would like to quit at any point enter nothing for the card name."
		while True:
			new = str(raw_input("Input Card Name: "))
			foundCard = self.findCard(new)
			if new =="":
				break
			elif foundCard != None:
				foundCard.increment()
			else:
				manaCost = list(raw_input("Input Mana Cost: "))
				quantity = int(raw_input("Input Quantity:  "))
				temp = card(new, manaCost, quantity)
				self.addCard(temp)
			print(new+" Added to collection")

			
			




class card:
	def __init__(self, name=None, cost=None, quantity=None):
		self.name = name			#str
		self.manaCost = cost		#list
		self.quantity = quantity	#int

	def __repr__(self):
		return self.name+" "+ ''.join(self.manaCost)+" # "+str(self.quantity)

	def isInCard(self, instr):
		#returns bool of a substring in the card name
		#fuzzy name finder
		if instr.lower() in self.name.lower():
			return True
		else:
			return False

	def isCard(self, instr):
		#returns bool exact name matching
		instr = instr.strip(" ")
		name = self.name.strip(" ")
		if instr.lower() == name.lower():
			return True
		else:
			return False

	def isCost(self, instr):
		#returns bool of equivalent cost
		if list(instr) == self.manaCost:
			return True
		else:
			return False

	def getQuantity(self):
		#return Quantity as an int
		return self.quantity
	
	def increment(self):
		self.quantity += 1

	def out(self):
		#returns for writing to a txt file
		# manaCost=""
		# for x in self.manaCost:
		# 	manaCost= manaCost+str(x)
		return (self.name+" ||| "+''.join(self.manaCost)+" ||| "+str(self.quantity)+"\n")














