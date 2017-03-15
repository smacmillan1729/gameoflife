import sys
import random
import drawGoL as draw

 #when do you need an object in class args?

"""
Joe's comments
	Line 30 is just an else

"""

class states(object):

	def __init__(self, initial = None):

		# if initial has been input 
		if(initial is not None):
			# if initial is an integer then create random square board
			if isinstance(initial, int):
				self.width = self.height = initial 
				self.states = self.makeRandom(self.width,self.height)

			# if initial is matrix, check board is valid and capture dimensions
			else:
				self.states = self.makeValidBoard(initial)
				self.width = len(self.states[0])
				self.height = len(self.states) 
				
		
		# if an initial has not been specified randomise an initial square board smaller than 20x20
		if(initial is None): 
			self.width  = self.height = random.randint(0, 20) 
			self.states = self.makeRandom()

		#class variables
		self.history = [self.states]    # List to store the history of the game
		self.equilib = False           # Check to see if an equilibrium has been reached
		
			
	def makeRandom(self,width,height):
		'''
		Randomise an initial board by creating a board of zero's and randomly giving each cell life
		'''
		randomStates = [[0 for y in range(width)] for x in range(height)]
		# generate random number in (0,1)
		r = random.random()
		# for each cell on board
		for i in range(0, width):
			for j in range(0, height):
				# if randomly generated number is bigger than prevously generated random number
				if random.random() > r:
					# give this cell life
					randomStates[i][j] = 1

		return randomStates

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
			drawB = draw.drawGoL(self.states,self.equilib, 'black', 'white')
			drawB.drawBoard()
		else:
			for row in self.states:
				print '\t'.join([str(x) for x in row])
			print ' '+'___'*self.width+'\n'	
			

