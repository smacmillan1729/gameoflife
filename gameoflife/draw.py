import turtle
import time


class drawGoL():
	def __init__(self,board,equilib = 0, cycleLength=0, liveColour = 'black',deadColour = 'white'):
		self.board = board
		self.cellsize = min(50,800.0/len(self.board))
		self.liveColour = liveColour
		self.deadColour = deadColour
		self.equilib = equilib
		self.cycleLength = cycleLength

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


	def square(self,colour):
		'''
		Draw one square of input colour
		'''
		Tim=self.Tim
		Tim.color(colour)
		Tim.begin_fill()
		for i in range(4):
			Tim.fd(self.cellsize)
			Tim.lt(90)
		Tim.end_fill()
		Tim.fd(self.cellsize)


	def drawRow(self,size,row):
		'''
		Draw one row of squares, with square colour depending on value of entry
		'''
		for i in row:
			if(i==1):
				self.square(self.liveColour)
			else:
				self.square(self.deadColour)
			


	def drawBoard(self):
		'''
		Draw the board
		'''
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
		
		# if the board being drawn is the last in the game
		#  exit upon click 
		if(not self.equilib):
			time.sleep(0.5)
		else: #(self.equilib==1):
			if(self.cycleLength == 1):
				self.window.title('Final state')
			else:
				title = 'Entered cycle of length ' + str(self.cycleLength)
				self.window.title(title)
			self.window.exitonclick()
