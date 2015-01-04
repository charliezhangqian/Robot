#!/usr/bin/python
import fileinput,sys
matrix = []
for line in sys.stdin.readlines():#read and store the map
	if not line.strip():
		continue
	lineNodes = line.split()
	matrix.append(lineNodes)

columns = len(matrix[0])
rows = len(matrix)

explored = []
priorityList = []
startNode = (0, 0)

def getSeccessors(node):
	successors = []
	if node[0] < columns - 1:
		successors.append((node[0]+1, node[1]))
	if node[1] < rows -1:
		successors.append((node[0], node[1]+1))
	if node[1] > 0:
		successors.append((node[0], node[1]-1))
	if node[0] > 0:
		successors.append((node[0]-1, node[1]))
	return successors

def my_cmp(E1,E2):
	return cmp(E1[2],E2[2])

priorityList.append((startNode, [], 0))

while(len(priorityList)):
	p = priorityList.pop(0)
	currentNode = p[0]

	moves = p[1]
	cost = p[2]

	if currentNode[0] == columns - 1 and currentNode[1] == rows - 1:
		print moves
		print cost
		break
	explored.append(currentNode)
	for n in getSeccessors(currentNode):
		if n not in explored:
			totalCost = cost + int(matrix[n[1]][n[0]], 16)
			if n[0] == currentNode[0] and n[1] == currentNode[1]+1:
				newMove = moves + ["d"]
			elif n[1] == currentNode[1] and n[0] == currentNode[0]+1:
				newMove = moves + ["r"]
			elif n[0] == currentNode[0] and n[1] == currentNode[1]-1:
				newMove = moves + ["u"]
			elif n[1] == currentNode[1] and n[0] == currentNode[0]-1:
				newMove = moves + ["l"]
			pos = -1
			for index in range(len(priorityList)):#check whether the neighbour is in the list
				if n == priorityList[index][0] and totalCost < priorityList[index][2]:
					pos = index
					break
			if pos != -1: #if it is in the list, update the cost to the lower cost
				priorityList[pos] = (n, newMove, totalCost)
			else:
				priorityList.append((n, newMove, totalCost))
	priorityList.sort(my_cmp)
