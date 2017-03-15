import sys
import random
import drawGoL as draw
import states

class Life():

	def __init__(self, initial):
		self.states = initial
		#class variables
		self.history = [self.states]    # List to store the history of the game
		self.equilib = False           # Check to see if an equilibrium has been reached

	def neighbourCount(self,x,y):  
		'''count alive neighbours'''
		count = 0
		# max/mins account for edge and corner cases
		for i in range( max(0, x-1), min(self.states.height, x+2) ):  
			for j in range( max(0, y-1), min(self.states.width, y+2) ):  

				# skip the middle point
				if (i == x and j == y):
					continue
				else:
					if(self.states[i][j]==1):
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
		newBoard = [[0 for y in range(self.states.width)] for x in range(self.states.height)] 
		 
		for i in range(self.states.height):
			for j in range(self.states.width):
				newBoard[i][j] = self.cellRules(i,j)

		# if newBoard is the same as the previous board we're in equilibrium
		if (self.states == newBoard):
			self.equilib = True 

		self.history.append(newBoard)	 
		return newBoard

	def evolve(self): 
		'''evolve (i.e iterate step until an equilibrium is reached, overwriting the input matrix'''
		# self.printBoard()
		
		while(self.equilib is False):
			self.board = self.singleStep()
			

	def printHistory(self):
		for h in self.history:
			print h
			




A = [[1,1,1],[1,0,1],[3,1,0],[0,0,1]]

B = states.states(A, False)
game = Life(B)
game.evolve()
#B.evolveInPlace()
# B.printHistory()



