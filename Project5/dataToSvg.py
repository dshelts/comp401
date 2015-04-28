#regular hex edge size 5inch
def writeSVG(filename, data):
	data = open(data, 'r')
	file = open(filename, 'w+')
	file.write('<svg version="1.1"\nbaseProfile="full"\nwidth="100%" height="100%"\nxmlns="http://www.w3.org/2000/svg">')
	file.write('\n<rect width="500" height="500" fill="white" />\n')
	#circleSize = []
	for line in data:
		values = line.split(',')
		sumTotal = 0
		radius = len(values)*3
		x = "250"
		y = "250"
		# for value in values:
		# 	sumTotal = sumTotal+int(value)
		# circleSize.append(sumTotal)	
	 
	#for value in circleSize:
		# radius = int(value)
		# radius = radius/5
		file.write('<circle cx="'+x+'" cy="'+y+'" r="'+str(radius)+'" stroke="black" stroke-width="1" fill="none" />\n')
	
				

	


	file.write('</svg>')

def main():

	data = 'disjnt2.txt'
	fileName = raw_input("Input a file name: ")
	fileName = str(fileName)
	fileName = fileName+'.svg'

	writeSVG(fileName, data)

if __name__ == '__main__':
	main()