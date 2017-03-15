import sys
import gen
import random


class Life(object):
	"""
	Sets up the initial input, keeps track of the game's history and implements evolution
	"""
	
	def __init__ (self, inputData=None) :
		self.setInitialBoard(inputData)
		self.history = [self.initialBoard]

	def setInitialBoard (self, inputData) :
		'''	
		Sets up the initial board instance, based on input
		'''
		if(inputData is not None):
			# If inputData is an integer then create random square board
			if isinstance(inputData, int):
				self.width = self.height = inputData 
				states = self.makeRandom()

			# If inputData is matrix, check board is valid and capture dimensions
			else:
				states = self.makeValidBoard(inputData)
				self.width = len(states[0])
				self.height = len(states) 
				
		# If an inputData has not been specified randomise an initial square board smaller than 20x20
		if(inputData is None): 
			self.width  = self.height = random.randint(0, 20) 
			states = self.makeRandom()

		# Create the initial instance of the board class
		initialBoard = gen.Generation(states)
		# Set the neighbour counts for that instance
		initialBoard.setNeighbourCounts()
		self.initialBoard = initialBoard

	def makeRandom(self):
		'''
		Randomise an initial board by creating a board of zero's and randomly giving each cell life
		'''
		states = [[0 for y in range(self.width)] for x in range(self.height)]
		# Generate random number in (0,1)
		r = random.random()
		# For each cell on board
		for i in range(0, self.width):
			for j in range(0, self.height):
				# If randomly generated number is bigger than prevously generated random number
				if random.random() > r:
					# Give this cell life
					states[i][j] = 1
		return states

	def makeValidBoard(self, array):
		'''
		Check that the board is valid (i.e containing only 0's and 1's)
		If board contains invalid elements, change elements > 1 to be 1 and < 0 to be 0 
		If any rows are shorter than the longest, pad them with 0's
		'''
		# Check size of all rows are equal
		maxwidth = len(max(array, key=len))
		for row in array:
			width = len(row)
			# If all rows are not equal
			if(width != maxwidth):
				diff = maxwidth - width
				# Pad shorter rows with 0's at end
				pad = [0] * diff
				row.extend(pad)

		# Check elements are valid
		for j in range(width):
			for i in range(len(array)):
				# If element positive set to alive
				if(array[i][j] >= 1):
					array[i][j] = 1
				# If element positive set to dead
				else:
					array[i][j] = 0

		return array

	def evolve (self):
		'''
		Computes the next step in the game's evolution
		'''
		# Get latest generation's states and neighbour count
		prevGen = self.history[-1]
		prevStates = prevGen.states
		prevNeighbours = prevGen.neighbours
		# Create next generation
		newGen = gen.Generation()
		newGen.setStates(prevStates, prevNeighbours)
		newGen.setNeighbourCounts()
		# Add next generation to history
		self.history.append(newGen)
		return newGen.states


	def checkEquilib (self) :
		'''
		Check if the game is in equilibrium
		i.e. if the last two states are the same
		'''
		lastGen = self.history[-1]
		lastStates = lastGen.states

		penultimateGen = self.history[-2]
		penultimateStates = penultimateGen.states

		return (lastGen == penultimateStates)

