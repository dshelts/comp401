import graph
def generatedGraph(size):
	g = graph.Graph(size)
	g.fillGraph()
	return g
def main():
	size = int(raw_input("raw_input size of graph: "))
	graph = generatedGraph(size)
	graph.printGraph()
if __name__ == '__main__':
	main()