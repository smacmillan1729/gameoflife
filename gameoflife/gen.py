

class Generation () :

	def __init__ (self, states = [], neighbours = []) :
		self.states = states;
		self.neighbours = neighbours;



	def setStates (self, prevStates, prevNeighbours) :
		'''
		Calculate states of current generation
		Based on the neighbour counts of the last generation (passed in)
		'''
		states = [[0 for y in range(len(prevStates[0]))] for x in range(len(prevStates))];

		for i in range (len(prevNeighbours)):
			row = prevNeighbours[i]
			for j in range (len(row)):
				countNeighbours = prevNeighbours[i][j]
				if(countNeighbours == 2):
					states[i][j] = prevStates[i][j] 
				elif(countNeighbours == 3):
					states[i][j] = 1
				else:
					states[i][j] = 0

		self.states = states


	def setNeighbourCounts (self):
		'''
		Store the neighbour counts of the current generation
		'''
		states = self.states
		neighbours = [[0 for y in range(len(self.states[0]))] for x in range(len(self.states))]
		for i in range (len (states)):
			row = states[i]
			for j in range (len (row)):
				neighbours[i][j] = self.countNeighbours(i, j)

		self.neighbours = neighbours


	def countNeighbours (self, i, j) :  
		'''
		Calculate how many neighbours the cell of the passed in position has
		'''
		count = 0
		for x in range( max(0, i - 1), min(len(self.states), i + 2) ):  
			for y in range( max(0, j - 1), min(len(self.states[0]), j + 2) ):  

				if (x == i and y == j):
					continue
				else:
					if( self.states[x][y] == 1):
						count = count + 1
		return count