#from life.py import Life
from gameoflife.Life import Life
import unittest

class testLife(unittest.TestCase):
	def test_no_interaction(self):
		empty = [  [0,0,0],
				   [0,0,0],
				   [0,0,0]  ]
		testEmpty = Life(empty)
		self.assertEqual(empty, testEmpty.evolve())


	def test_lonely(self):
		empty = [  [0,0,0],
				   [0,0,0],
				   [0,0,0]  ]
		lonely = [[0,0,0],[0,1,0],[0,0,0]]
		testLonely = Life(lonely)
		self.assertEqual(empty, testLonely.evolve())

	def test_non_rect(self):
		nonRect = [  [1,0,0,1],
				     [1,0,0  ],
				     [0,1,1,1]  ]
		nonRE =  [[0, 0, 0, 0 ],
		          [1, 0, 0, 1 ],
		          [0, 1, 1, 0]]
		testNR = Life(nonRect)
		self.assertEqual(nonRE, testNR.evolve())

	def test_stays_alive(self):
		row = [  [0,0,0],
				 [1,1,1],
				 [0,0,0]  ]

		col = [  [0,1,0],
				 [0,1,0],
				 [0,1,0]  ]
		testRow = Life(row)
		self.assertEqual(col, testRow.evolve())


	def test_overcrowded(self):
		full = [  [1,1,1],
				  [1,1,1],
				  [1,1,1]  ]
		corners = [[1, 0, 1],
		           [0, 0, 0],
		           [1, 0, 1]]
		testFull = Life(full)
		self.assertEqual(corners,testFull.evolve())

	def test_new_life(self):
		corners = [[1, 0, 1],
		           [0, 0, 0],
		           [1, 0, 1]]
		empty = [  [0,0,0],
				   [0,0,0],
				   [0,0,0]  ]
		testCorners = Life(corners)
		self.assertEqual(empty,testCorners.evolve())

	def test_invalid_input(self):
		matrix =   [[-1, 0, 0],
		           [3, 2, 1],
		           [0, 0, 0]]   #should be read as the same as row in test_stays_alive
		col = [  [0,1,0],
				 [0,1,0],
				 [0,1,0]  ]
		testMatrix = Life(matrix)
		self.assertEqual(col,testMatrix.evolve())