import sys
import random
import drawGoL as draw

 #when do you need an object in class args?



class Life(object):

	def __init__(self, initial = None, graphics = True):

		# if initial has been input 
		if(initial is not None):
			# if initial is an integer then create random square board
			if isinstance(initial, int):
				self.width = self.height = initial 
				self.board = self.makeRandom()

			# if initial is matrix, check board is valid and capture dimensions
			else:
				self.board = self.makeValidBoard(initial)
				self.width = len(self.board[0])
				self.height = len(self.board) 
				
		
		# if an initial has not been specified randomise an initial square board smaller than 20x20
		if(initial is None): 
			self.width  = self.height = random.randint(0, 20) 
			self.board = self.makeRandom()

		#class variables
		self.history = [self.board]    # List to store the history of the game
		self.equilib = False           # Check to see if an equilibrium has been reached
		self.graphics = graphics       # Bool to see whether to display graphics
		
			
	def makeRandom(self):
		'''
		Randomise an initial board by creating a board of zero's and randomly giving each cell life
		'''
		self.board = [[0 for y in range(self.width)] for x in range(self.height)]
		# generate random number in (0,1)
		r = random.random()
		# for each cell on board
		for i in range(0, self.width):
			for j in range(0, self.height):
				# if randomly generated number is bigger than prevously generated random number
				if random.random() > r:
					# give this cell life
					self.board[i][j] = 1
		return self.board

	def makeValidBoard(self, A):
		'''
		Check that the board is valid (i.e containing only 0's and 1's)
		If board contains invalid elements, change elements > 1 to be 1 and < 0 to be 0 
		If any rows are shorter than the longest, pad them with 0's
		'''
		# check size of all rows are equal
		maxwidth = len(max(A,key=len))
		for row in A:
			width = len(row)
			# if all rows are not equal
			if(width != maxwidth):
				diff = maxwidth - width
				# pad shorter rows with 0's at end
				a = [0] * diff
				row.extend(a)

		# check elements are valid
		for j in range(width):
			for i in range(len(A)):
				if(A[i][j] not in [0,1]):
					# if element positive set to alive
					if(A[i][j]>1):
						A[i][j] = 1
					# if element positive set to dead
					else:
						A[i][j] = 0

		return A

	def displayBoard(self):
		'''
		If graphics are on, display the board using the drawGOL class
		If graphics are off, print the output
		'''
		if(self.graphics):
			drawB = draw.drawGoL(self.board,self.equilib, 'black', 'white')
			drawB.drawBoard()
		else:
			for row in self.board:
				print '\t'.join([str(x) for x in row])
			print ' '+'___'*self.width+'\n'	



	def neighbourCount(self,x,y):  
		'''count alive neighbours'''
		count = 0
		# max/mins account for edge and corner cases
		for i in range( max(0, x-1), min(self.height, x+2) ):  
			for j in range( max(0, y-1), min(self.width, y+2) ):  

				# skip the middle point
				if (i == x and j == y):
					continue
				else:
					if( self.board[i][j]==1):
						count = count + 1
		return count


	def cellRules(self,xcell,ycell):
		liveneighbours = self.neighbourCount(xcell,ycell)
		if(liveneighbours <2 or liveneighbours > 3 ):
			return 0
		elif (liveneighbours == 2):
			return self.board[xcell][ycell]
		elif (liveneighbours == 3):
			return 1

	def singleStep (self): 
		'''implement one evoluation'''
		newBoard = [[0 for y in range(self.width)] for x in range(self.height)] 
		 
		for i in range(self.height):
			for j in range(self.width):
				newBoard[i][j] = self.cellRules(i,j)

		# if newBoard is the same as the previous board we're in equilibrium
		if (self.board == newBoard):
			self.equilib = True 

		self.history.append(newBoard)	 
		return newBoard

	def evolveInPlace(self): 
		'''evolve (i.e iterate step until an equilibrium is reached, overwriting the input matrix'''
		# self.printBoard()
		self.displayBoard()
		while(self.equilib is False):
			self.board = self.singleStep()
			self.displayBoard()	

	def printHistory(self):
		for h in self.history:
			print h
			




A = [[1,1,1],[1,0,1],[3,1,0],[0,0,1]]

B = Life(100, True)
B.evolveInPlace()
# B.printHistory()



