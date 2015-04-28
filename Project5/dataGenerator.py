#SeniorSem1_1.py
#disjoint data set
from random import randint


class Element():
	def __init__(self, item = None, next = None, prev = None, link = None):
		self.value = item
		self.next = next
		self.prev = prev
		self.link = link

	def getValue(self):
		return self.value
	def setNext(self, next):
		self.next = next
	def getNext(self):
		return self.next
	def setPrev(self, prev):
		self.prev = prev
	def getPrev(self):
		return self.prev
	def setLink(self, link):
		self.link = link
	def getLink(self):
		return self.link

class DisjointSet():
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def append(self, represent):
		#left to right 
		if self.head == None:
			self.head = represent
			self.tail = represent
			self.size = self.size + 1
		else:
			represent.setPrev(self.tail)
			self.tail.setNext(represent)
			self.tail = represent
			self.size = self.size+1

	def union(self):
		#chaining down
		if self.size <= 1:
			print "Nothing left to union"
	
		else:
			ranint1 = randint(0, self.size-1)
			ranint2 = randint(0, self.size-1)
			
			while ranint1 == ranint2:
				ranint2 = randint(0, self.size-1)
			
		
			#get the representative
			temp = self.head
			for i in xrange(0, ranint1):
				temp = temp.getNext()
			rep = temp					#representative to add to
			

			temp = self.head
			for i in xrange(0, ranint2):
				temp = temp.getNext()
			chain = temp					#get the chain to add to your representative
			
			
			#y is the end of the list x, y set x to tail
			if chain.getNext() == None:
				x = chain.getPrev()
				x.setNext(None)
				self.tail = x
				chain.setPrev(None)
			#head of the list	
			elif chain.getPrev() == None:
				x = chain.getNext()
				x.setPrev(None)
				self.head = x
				chain.setNext(None)
			# removing  y from the  list
			else:
				z = chain.getNext()
				x = chain.getPrev()

				x.setNext(z)#x->z
				z.setPrev(x)#x<-z
				chain.setNext(None)
				chain.setPrev(None)	
			self.size = self.size - 1 # disjoint set is one rep smaller
			
			#adding the chain to the end of the representative list
			temp = rep
			while temp.getLink() != None:
				temp = temp.getLink()
			
			temp.setLink(chain)

	def display(self):
		x = self.head
		for i in xrange(0, self.size):
			displaySubset(x)
			print "|"
			x = x.getNext()
		print "Done"

	def find(self, value):
		x = self.head
		for i in xrange(0, self.size):
			y = x
			while y.getLink() != None:
				if y.getValue() == value:
					return x #returns the representative of the value
				else:
					y = y.getLink()
			if y.getValue() == value:
					return x #returns the representative of the value
			else:
				y = y.getLink()

			x = x.getNext()

		print value, " not found"

		
	def getSize(self):
		return self.size

	def writeToFile(self):
		file = open('disjnt2.txt', 'w+')
		x = self.head
		for i in xrange(0, self.size):
			y = x
			# file.write(str(y.getValue())+', ')
			while y.getLink() != None:
				file.write(str(y.getValue()) + ', ')
				y = y.getLink()
			file.write(str(y.getValue())+ '\n')
			x = x.getNext()
		



			



def makeSet(disjointset ,size):
	for i in xrange(size):
		rep = Element(i)
		disjointset.append(rep)

def displaySubset(set):
	temp = set
	while temp.getLink() != None:
		print temp.getValue(),"->",
		temp = temp.getLink()
	print temp.getValue(), "-> None"
	
def unionSet(set, number):
	for i in xrange (number):
		set.union()





def main():
	disjnt = DisjointSet()
	makeSet(disjnt, 10000)
	unionSet(disjnt, 8750)
	#print "display"
	#disjnt.display()
	disjnt.writeToFile()

if __name__ == '__main__':
	main()


