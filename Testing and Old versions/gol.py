import sys
import random
import drawGoL as draw



class Life ():
	"""
	Sets up the initial input, keeps track of the game's history and implements evolution
	"""
	
	def __init__ (self, inputArray=None) :
		self.setInitialBoard(inputArray)
		self.history = [self.initialBoard]

	def setInitialBoard (self, inputArray) :
		if(inputArray is not None):
			# if inputArray is an integer then create random square board
			if isinstance(inputArray, int):
				print "Made It"
				self.width = self.height = inputArray 
				states = self.makeRandom()

			# if inputArray is matrix, check board is valid and capture dimensions
			else:
				states = self.makeValidBoard(inputArray)
				self.width = len(states[0])
				self.height = len(states) 
				
		# if an inputArray has not been specified randomise an initial square board smaller than 20x20
		if(inputArray is None): 
			self.width  = self.height = random.randint(0, 20) 
			states = self.makeRandom()


		initialBoard = Board(states)
		initialBoard.setNeighbourCounts()
		self.initialBoard = initialBoard

	def makeRandom(self):
		'''
		Randomise an initial board by creating a board of zero's and randomly giving each cell life
		'''
		states = [[0 for y in range(self.width)] for x in range(self.height)]
		# generate random number in (0,1)
		r = random.random()
		# for each cell on board
		for i in range(0, self.width):
			for j in range(0, self.height):
				# if randomly generated number is bigger than prevously generated random number
				if random.random() > r:
					# give this cell life
					states[i][j] = 1
		return states

	def makeValidBoard(self, array):
		'''
		Check that the board is valid (i.e containing only 0's and 1's)
		If board contains invalid elements, change elements > 1 to be 1 and < 0 to be 0 
		If any rows are shorter than the longest, pad them with 0's
		'''
		# check size of all rows are equal
		maxwidth = len(max(array, key=len))
		for row in array:
			width = len(row)
			# if all rows are not equal
			if(width != maxwidth):
				diff = maxwidth - width
				# pad shorter rows with 0's at end
				pad = [0] * diff
				row.extend(pad)

		# check elements are valid
		for j in range(width):
			for i in range(len(array)):
				# if element positive set to alive
				if(array[i][j] >= 1):
					array[i][j] = 1
				# if element positive set to dead
				else:
					array[i][j] = 0

		return array

	def nextStep (self):
		prevBoard = self.history[-1]
		prevStates = prevBoard.states
		prevNeighbours = prevBoard.neighbours
		newBoard = Board()
		newBoard.setStates(prevStates, prevNeighbours)
		newBoard.setNeighbourCounts()
		self.history.append(newBoard)


	def checkEquilib (self) :
		prevBoard = self.history[-1]
		penultimateBoard = self.history[-2]
		prevStates = prevBoard.states
		penultimateStates = penultimateBoard.states
		return (prevStates == penultimateStates)



class Board () :

	def __init__ (self, states = [], neighbours = []) :
		self.states = states;
		self.neighbours = neighbours;


	def setStates (self, prevStates, prevNeighbours) :
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
		states = self.states
		neighbours = [[0 for y in range(len(self.states[0]))] for x in range(len(self.states))]
		for i in range (len (states)):
			row = states[i]
			for j in range (len (row)):
				neighbours[i][j] = self.countNeighbours(i, j)

		self.neighbours = neighbours


	def countNeighbours (self, i, j) :  
		count = 0
		for x in range( max(0, i - 1), min(len(self.states), i + 2) ):  
			for y in range( max(0, j - 1), min(len(self.states[0]), j + 2) ):  

				if (x == i and y == j):
					continue
				else:
					if( self.states[x][y] == 1):
						count = count + 1
		return count


def main(inputArray):

	life = Life(inputArray)


	stop = False
	count = 0

	while (not hasCycled):
		count += 1
		life.nextStep()
		lastStates = life.history[-1].states

		stop = checkIfCycled(life.history) and count < 150

		# COULD DRAW GRAPHICS HERE. ORRRR WAIT UNTIL THE END AND DRAW THEM ALL.
		# Pass height and width into the constructor for Board and use instead of calculation over and over
		# stop = life.checkEquilib() and count < 100 ;


	for i in range(len(life.history)) :
		states = life.history[i].states



		drawB = draw.drawGoL(states, (i == len(life.history) - 1))
		drawB.drawBoard()

		print states


def checkIfCycled(history) :
	hasCycled = False
	for x in range(2, len(history)) :
		if (history[-1].states == history[-x].states) :
			hasCycled = True
			break
	return hasCycled

inputNumber = 100
inputArray = [[1,0,0,1], [1, 0, 0, 0], [0, 1, 1, 1]]
main(inputNumber)


