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
			ranint1 = randint(0, self.size)
			ranint2 = randint(0, self.size)
			
			while ranint1 == ranint2:
				ranint2 = randint(0, self.size)
			
			#get the representative
			temp = self.head
			for i in xrange(0, ranint1):
				temp = temp.getNext()
			rep = temp					#representative to add to

			temp = self.head
			for i in xrange(0, randit2):
				temp = temp.getNext()
			chain = temp					#get the chain to add to your representative
			
			
			# removing  y from the left to right list
			if chain.getNext() != None:
				z = chain.getNext()
				x = chain.getPrev()

				x.setNext(z)#x->z
				z.setPrev(x)#x<-z
				chain.setNext(None)
				chain.setPrev(None)
			#y is the end of the list x, y set x to tail
			else:
				x = chain.getPrev()
				x.setNext(None)
				self.tail = x
				chain.setPrev(None)
			self.size = self.size - 1 # disjoint set is one rep smaller
			
			#adding the chain to the end of the representative list
			temp = rep
			while temp.getLink() != None:
				temp = temp.getLink()
			temp.setLink(chain)






			



def makeSet(self, disjointset ,size):
	for i in xrange(size):
		rep = Element(i)
		disjointset.append(rep)










def main():
	for i in xrange(0, 6):
		print i
	
if __name__ == '__main__':
	main()


