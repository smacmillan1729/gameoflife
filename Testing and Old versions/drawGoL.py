import turtle
import time


class drawGoL():
	def __init__(self,board,equilib = False, liveColour = 'black',deadColour = 'white'):
		self.board = board
		self.cellsize = min(50,800.0/len(self.board))
		self.liveColour = liveColour
		self.deadColour = deadColour
		self.equilib = equilib

		#setup screen
		self.window = turtle.Screen()
		self.window.bgcolor('lightgray')
		self.window.title('Game Of Life')
		turtle.setup(800, 800)
		cellSize = min(50,800.0/len(self.board))

		#setup turtle
		self.Tim=turtle.Turtle(visible=False)
		self.Tim.speed(0)
		self.Tim.tracer(False) 
		self.Tim.color("black")

	#draw one square
	def square(self,colour):
		Tim=self.Tim
		Tim.color(colour)
		Tim.begin_fill()
		for i in range(4):
			Tim.fd(self.cellsize)
			Tim.lt(90)
		Tim.end_fill()
		Tim.fd(self.cellsize)


	def drawRow(self,size,row):
		for i in row:
			if(i==1):
				self.square(self.liveColour)
			else:
				self.square(self.deadColour)
			


	def drawBoard(self):
		Tim = self.Tim
		size = self.cellsize
		board = self.board
		height = len(board) 
		width = len(board[0])
		Tim.pu()
		Tim.goto(-(size*(height/2.0)),(size*(width/2.0)))

		for i in range(height):
			self.drawRow(size,board[i])
			Tim.bk(size*width)
			Tim.rt(90)
			Tim.fd(size)
			Tim.lt(90)
		

		if(self.equilib):
			self.window.title('Final state')
			self.window.exitonclick()
		else:

			time.sleep(0.5)
		


#for row in B:
#	print "\t".join([str(x) for x in row])

#L = [[0,1],[1,0],[1,1]]
#DL = drawGoL(L,False)

#DL.drawBoard()

