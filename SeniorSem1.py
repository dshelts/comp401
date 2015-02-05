class Set():
	def __init__(self):
		#Empty constructor
		self.set = []
	
	def append(self, x):
		#append
		inlist = False
		for ele in self.set:
			if x == ele:#if element in set
				inlist = True
				break
		if inlist == False:
			self.set.append(x)

	def addlist(self, array):
		#takes an array and adds the elements to a set
		for ele in array:
			self.append(ele)
		

	def union(self, visitingSet):
		temp = Set()
		temp.addlist(self.set)
		temp.addlist(visitingSet.set)
		return temp

	def intersection(self, visitingSet):
		temp = Set()
		for ele1 in self.set:
			for ele2 in visitingSet.set:
				if ele1 == ele2:
					temp.append(ele1)
				else:
					pass
		return temp

	def setorder(self):
		#find size of set
		return len(self.set)

	def viewset(self):
		#stringify the set
		outstr = "{"
		for ele in self.set:
			concat = str(ele) + ", "# "i, "
			outstr += concat
		return outstr.rstrip(', ') +'}'
	
	




def main():
	A = Set()
	B = Set()
	C = Set()

	A.addlist([1,2,3,4])
	B.addlist([1,3,5,7,9])
	C.addlist([2,4,6,8,10])
	
	
	
	print "AUC" 
	print A.union(C).viewset()
	print "AUB"
	print A.union(B).viewset()
	print "BUC"
	print B.union(C).viewset()
	print "A intersection B"
	print A.intersection(B).viewset()
	print "B intersection C"
	print B.intersection(C).viewset()
	print "A intersection C"
	print A.intersection(C).viewset()
	print "A intersection A"
	print A.intersection(A).viewset()


if __name__ == '__main__':
		main()