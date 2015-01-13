#!/usr/bin/python
#encoded: 
#######################################################################
#This program is able to find the least cost path for the robot.It    #
#starts from the left top node and finds its successors. For each     #
#successing node, calculate it accumulated cost along the path from   # 
#starting node to this node. These nodes are sorted based on cost in  #
#the ascending sequence. So each expension will search the least cost #
#node first. When the ending node meet, the algorithm stops and output#
#the path.                                                            #
#The algorithm is a tree search algorithm used for traversing or      #
#searching a weighted tree or graph. The search continues by visiting #
#the next node which has the least total cost from the root.          #
#It is complete and optimal if the cost of each step exceeds some     #
#positive bound x.The worst-case time and space complexity is         #
#O(b^(1 + C*/x)), where C* is the cost of the optimal solution and b is 
#the branching factor.                                                #
#######################################################################
import fileinput,sys

class pathSearch(object):
	explored = []      #to store the nodes that have been explored
	priorityList = []  #priorityList always pop the next least cost node
	matrix = []        #the matrix is to store the map
	startNode = (0, 0)
	columns = 0        #columns of the map
	rows = 0           #rows of the map
	endNode = (-1, -1)

	def __init__(self):
		self.loadMap()
		self.columns = len(self.matrix[0])
		self.rows = len(self.matrix)
		self.endNode = (self.columns - 1, self.rows - 1)
		self.priorityList.append((self.startNode, [], 0))

	#this function reads the map from standard input
	def loadMap(self):
		for line in sys.stdin.readlines():
			if not line.strip():
				continue
			lineNodes = line.split()
			self.matrix.append(lineNodes)
		return self.matrix

	# this function used for comparison in prorityList
	def my_cmp(self, E1,E2):
		return cmp(E1[2],E2[2])

	# this function get all the successors of a node
	def getSeccessors(self, node):
		successors = []
		if node[0] < self.columns - 1:
			successors.append((node[0]+1, node[1]))
		if node[1] < self.rows -1:
			successors.append((node[0], node[1]+1))
		if node[1] > 0:
			successors.append((node[0], node[1]-1))
		if node[0] > 0:
			successors.append((node[0]-1, node[1]))
		return successors

	#This function find the direciton of move between two nodes
	def move(self, node1,node2):
		if node1[0] == node2[0] and node1[1] == node2[1]+1:
			return "d"
		elif node1[1] == node2[1] and node1[0] == node2[0]+1:
			return "r"
		elif node1[0] == node2[0] and node1[1] == node2[1]-1:
			return "u"
		elif node1[1] == node2[1] and node1[0] == node2[0]-1:
			return "l"

	#This function store the successors into the priorityList.
	#If the new node is already in list, check whether it has 
	#the low cost. If it does, update the old node with the new
	#moves and new cost. Otherwise, reject it.
	#If the new node is not in list, just append to it.
	def updatePriorityList(self, node, totalCost, newMove):
		pos = -1
		for index in range(len(self.priorityList)):
			if node == self.priorityList[index][0] and totalCost < self.priorityList[index][2]:
				pos = index
				break
		if pos != -1:
			self.priorityList[pos] = (node, newMove, totalCost)
		else:
			self.priorityList.append((node, newMove, totalCost))
			
	#Pop the least cost node from the priorityList and explore its
	#successors. Keep doing this untill the ending node is found.
	def findPath(self):
		while(len(self.priorityList)):
			p = self.priorityList.pop(0)
			currentNode = p[0]
			moves = p[1]
			cost = p[2]
			if currentNode == self.endNode:
				return moves
			self.explored.append(currentNode)
			for n in self.getSeccessors(currentNode):
				if n not in self.explored:
					totalCost = cost + int(self.matrix[n[1]][n[0]], 16)
					m = self.move(n, currentNode)
					newMove = moves + [m]
					self.updatePriorityList(n, totalCost, newMove)
			self.priorityList.sort(self.my_cmp)

def main():
	instance = pathSearch()
	path = instance.findPath()
	print ",".join(path)

if __name__ == "__main__":
	main()
