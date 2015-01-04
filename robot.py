#!/usr/bin/python
import fileinput,sys
matrix = []
for line in sys.stdin.readlines():
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
			if n[0] == currentNode[0]:
				newMove = moves + ["d"]
			elif n[1] == currentNode[1]:
				newMove = moves + ["r"]
			pos = -1
			for index in range(len(priorityList)):
				if n == priorityList[index][0] and totalCost < priorityList[index][2]:
					pos = index
					break
			if pos != -1:
				priorityList[pos] = (n, newMove, totalCost)
			else:
				priorityList.append((n, newMove, totalCost))
	priorityList.sort(my_cmp)
