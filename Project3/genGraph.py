import graph
import reverseDelete
def generatedGraph(size):
	g = graph.Graph(size)
	g.fillGraph()
	return g
def main():
	size = int(raw_input("raw_input size of graph: "))
	testGraph = generatedGraph(size)
	#testGraph.printGraph()
	reverseDelete.reverse_Delete(testGraph)
if __name__ == '__main__':
	main()