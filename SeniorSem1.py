class Set(object):
	def __init__(self):
		self.set = []
	
	def append(self, x):
		inlist = False
		for y in self.set:
			if x == y:#if element in set
				inlist = True
				break
		if inlist == False:
			self.set.append(x)

	def viewset(self):
		outstr = "{"
		for x in self.set:
			concat = str(x) + ", "# "i, "
			outstr += concat
		
		return outstr.rstrip(', ') +'}'

def main():
	A = Set()
	B = Set()

	for i in xrange(5):
		A.append(i)
		B.append(i)
	for i in xrange(9):
		A.append(i)

	print A.viewset()
	print B.viewset()

if __name__ == '__main__':
		main()