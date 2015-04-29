import random

class Graph():

	class Node():
		def __init__(self, name = None):
			self.name = name
			self.edges = []
			
		def getName(self):
			return self.name #return name as string
		def getEdges(self):
			return self.edges  #returns an array of edges distinct to the currently selected node
		def appendEdge(self, edge):
			self.edges.append(edge) #append an edge to a Node

	class Edge():
		def __init__(self, node=None,weight=None, connection = None):
			self.node = node
			self.weight = weight
			self.connection = connection
		def getNode(self):
			return self.node
		def getWeight(self):
			return self.weight
		
		def getConnection(self):
			return self.connection
		
	def __init__(self,  size = None):
		self.graph = []
		self.size = size

	def fillGraph(self):
		for i in range(0, self.size):
			temp = self.Node("node "+str(i))
			self.graph.append(temp)
			#Create nodes for the graph

		numConnected = int(self.size*3.14) #abitrary number of connections
		for i in range(0, numConnected):
			#connect the nodes in the graph
			weight   = random.randint(1,20)#weight of edge
			strtNode = random.choice(self.graph)#node ->
			destNode = random.choice(self.graph)#->node
			destNode = destNode.getName()#str of node name
			tempEdge = self.Edge(strtNode, weight, destNode)
			strtNode.appendEdge(tempEdge)

	def printGraph(self):
		for node in self.graph:
			print node.getName(),"[ ",
			edges = node.getEdges()  #returns an array of edges distinct to the currently selected node
			for edge in edges:
				print "(",edge.getWeight(), edge.getConnection(),")",
			print " ]"
	def getGraph(self):
		return self.graph


			