# The game of life

A python implementation of [Conway's game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), with an optional graphical display.


To play the game: 

```def playGame(inputArray, graphics, iterationLimit):```


param | default | |
--- | --- | ---
`input array` | Randomly generated board of any size | A matrix representing the initial state of the board. If invalid, the board is padded with zeros, and assumes any value > 1 should be alive, and any value < 0 should be dead.
`graphics` | `True` | Determines whether the resulting game should be drawn using turtle. If false game is displayed in terminal.
`iterationLimit` | `250` | The iteration limit. Game will end sooner if it enters its final state before the limit.