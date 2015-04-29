def compare(obj1, obj2):
	val1 = obj1.getWeight()
	val2 = obj2.getWeight()
	if val1 >= val2:
		return 1
	else:
		return -1

def printEdges(arrayOfEdges):
	print "[ ",
	for edge in arrayOfEdges:
		print "(",edge.getWeight(), edge.getConnection(),")",
	print" ]"

def getAllEdges(graph):
	allEdges = []
	graph = graph
	for node in graph:#get each node
		node = node.getEdges()#list of edges connected to node
		for edge in node:
			allEdges.append(edge)#creating a complete list of all graph edges
	sortedEdges = sorted(allEdges, cmp=compare, reverse=True)#sorts edges in descending order
	return sortedEdges

def reverse_Delete(graph):
	#take a graph object
	graph = graph.getGraph()#iterable list of nodes
	allEdges = getAllEdges(graph)#iterable list of edge objects sorted in descending order
	
	i = 0
	while i < len(allEdges):
		edge = allEdges[i]
		strt = edge.getNode()#str starting node
		weight = edge.getWeight()#weight of edge
		dest = edge.getConnection()
		#if it will futher disconnect node from graph skip
		#else del allEdges[i]
		i = i + 1
	return allEdges