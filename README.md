Robot
=====
This program is able to find the least cost path for the robot.It starts from the left top node and finds its successors. For each successing node, calculate it accumulated cost along the path from #starting node to this node. These nodes are sorted based on cost in the ascending sequence. So each expension will search the least cost node first. When the ending node meet, the algorithm stops and output the path.

The algorithm is a tree search algorithm used for traversing or searching a weighted tree or graph. The search continues by visiting the next node which has the least total cost from the root.

It is complete and optimal if the cost of each step exceeds some #positive bound x.The worst-case time and space complexity is O(b^(1 + C*/x)), where C* is the cost of the optimal solution and b is the branching factor.

Usage:
python robot_ex.py < test2
Output:
r,r,d,d,r,d,d,r,r,d

Unittest:
python tests.py < test2

