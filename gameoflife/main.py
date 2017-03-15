import gen
import Life
import draw

def playGame(inputArray, graphics = True, iterationLimit = 250):

	# Start the game
	game = Life.Life(inputArray)

	#counts to prevent infinite cycle
	stop = False
	count = 0

	# Run evolution until 150 life cycles, or we enter a cycle
	while (not stop):
		count += 1
		game.evolve()
		lastGen = game.history[-1].states

		cycleLength = checkIfCycled(game.history)

		stop = ((cycleLength!=0) and count < iterationLimit)

	# Display output for saved generations in game
	for i in range(len(game.history)) :
		states = game.history[i].states
		inEquilib = (i == len(game.history) - 1)
		displayBoard(states,inEquilib, cycleLength,graphics)


def displayBoard(board, equilib, cycleLength, graphics=True):
		'''
		If graphics are on, display the board using the drawGOL class
		If graphics are off, print the output
		'''
		if(graphics):
			drawB = draw.drawGoL(board,equilib,cycleLength, 'black', 'white')
			drawB.drawBoard()
		else:
			for row in board:
				print '\t'.join([str(x) for x in row])
			print ' '+'___'*len(row)+'\n'
			# Print useful information about game state
			if(equilib and cycleLength==1):
				print 'Reached Final State'
			elif(equilib and cycleLength>1):
				print 'Life has entered a cycle of length', cycleLength


def checkIfCycled(history) :
	'''
	Check if game has been a state before, hence has entered a cycle
	'''
	hasCycled = 0
	for x in range(2, len(history)) :
		if (history[-1].states == history[-x].states) :
			hasCycled = x-1
			break
	return hasCycled



inputArray = [[1,0,0,1], [1, 0, 0], [0, 1, 1, 1]]
#inputArray2 = [[0,0,0], [1, 1, 1], [0, 0, 0]]
playGame(inputArray, True)


