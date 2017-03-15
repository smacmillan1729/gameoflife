import sys
import random
import drawGoL as draw


class Life(object):

	"""constructor"""
	def __init__(self,initial = None, graphics = True):

		self.equilib = False #check to see if an equilibrium has been reached
		self.graphics = graphics

		#if initial has been specified 
		if(initial is not None):
			#if input an integer create random square board
			if isinstance( initial, int ):
				self.width = self.height = initial 
				self.board = self.makeRandom()

			#if input a matrix, check board is valid and capture dimensions
			else:
				self.board = self.makeValidBoard(initial)
				self.width = len(self.board[0])
				self.height = len(self.board) 
				
		
		#if an initial matrix has not been specified randomise an initial board smaller than 20x20
		if(initial is None): 
			self.width = random.randint(0, 20) 
			self.height = random.randint(0, 20)
			self.board = self.makeRandom()
		
			
	def makeRandom(self):
		'''Randomise an initial board by creating a board of zero's and randomly giving each cell life'''
		self.board = [[0 for y in range(self.width)] for x in range(self.height)]
		#generate random number in (0,1)
		r = random.random()
		#for each cell on board
		for i in range(0, self.width):
			for j in range(0, self.height):
				#if randomly generated number is bigger than prevously generated random number
				if random.random() > r:
					#give this cell life
					self.switchLife(i, j)
		return self.board

	def makeValidBoard(self, A):
		'''Check that the board is valid (i.e containing only 0's and 1's)
		   If any rows are shorter than the longest, pad them with 0's
		'''
		#check size
		maxwidth = len(max(A,key=len))
		for row in A:
			width = len(row)
			if(width != maxwidth):
				diff = maxwidth - width
				a = [0] * diff
				row.extend(a)
			for c in row:
				if(c!=0 or c!=1):
					c = 0
		#check elements (assume alive unless negative)
		for j in range(width):
			for i in range(len(A)):
				if(A[i][j] not in [0,1]):
					if(A[i][j]>1):
						A[i][j] = 1
					else:
						A[i][j] = 0

		return A
	"""
	def printBoard(self):  
		'''print the board'''
		for row in self.board:
			print '\t'.join([str(x) for x in row])

	def visualiseBoard(self):
		drawB = draw.drawGoL(self.board,self.equilib, 'black', 'white')
		drawB.drawBoard()
	"""

	def displayBoard(self):
		if(self.graphics):
			drawB = draw.drawGoL(self.board,self.equilib, 'black', 'white')
			drawB.drawBoard()
		else:
			'''print the board'''
			for row in self.board:
				print '\t'.join([str(x) for x in row])
			print ' '+'___'*self.width+'\n'	

	def switchLife(self, x, y):  
		'''toggle the status of the cell'''
		self.board[x][y] = 1

	def neighbourCount(self,x,y):  
		'''count alive neighbours'''
		count = 0
		#max/mins account for edge and corner cases
		for i in range( max(0, x-1), min(self.height, x+2) ):  
			for j in range( max(0, y-1), min(self.width, y+2) ):  

				#skip the middle point
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

		#if newBoard is the same as the previous board we're in equilibrium
		if (self.board == newBoard):
			self.equilib = True  
		return newBoard

	def evolveInPlace(self): 
		'''evolve (i.e iterate step until an equilibrium is reached, overwriting the input matrix'''
		#self.printBoard()
		self.displayBoard()
		while(self.equilib is False):
			self.board = self.singleStep()
			self.displayBoard()	



	def evolve(self):
		History = [self.board] 
		mostrecent = self.board
		i = 0

		while(self.equilib == False and i<15 ):

			Latest = Life(mostrecent)
			nextgen = Latest.singleStep()

			#print History[-1]
			#print nextgen.singleStep()
			History.append(nextgen)

			if (mostrecent == nextgen):
			#	print self.equilib
				self.equilib = True
			mostrecent = nextgen 
			i = i + 1

			print self.equilib

		for h in History:
			"""
			hB = Life(h, self.graphics)
			hB.displayBoard()
			"""

	






A = [[1,1,1],[1,0,1],[3,1,0],[0,0,1]]

B = Life(A, True)
B.evolve()

