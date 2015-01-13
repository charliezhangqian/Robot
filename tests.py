import unittest
from robot_ex import pathSearch

#this is the unittest program, testing all the functions in robot_ex.py
class Test(unittest.TestCase):
	def setUp(self):
		pass

	def test_loadMap(self):
		instance = pathSearch()
		assert(len(instance.loadMap()) != 0)

	def test_cmp(self):
		instance = pathSearch()
		result = instance.my_cmp(((0,0), ['r'], 4), ((1,1),['r','d'],5))
		assert(result < 0)

	def test_getSuccessors(self):
		instance = pathSearch()
		result = instance.getSeccessors((0,0))
		assert(len(result) == 2)

	def test_getSuccessors2(self):
		instance = pathSearch()
		result = instance.getSeccessors((1,1))
		assert(len(result) == 4)

	def test_move(self):
		instance = pathSearch()
		result = instance.move((0,1),(0,0))
		assert(result == "d")

	def test_updatePriorityList(self):
		instance = pathSearch()
		instance.priorityList = [((0,0), [], 0), ((2,3),[],3)]
		instance.updatePriorityList((2,3),2,["r"])
		assert(self.instance.priorityList == [((0,0), [], 0), ((2,3),["r"],2)])

if __name__ == '__main__':
	unittest.main()