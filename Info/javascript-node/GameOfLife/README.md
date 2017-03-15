## Task ##

Your task is to implement the rules of Conway's Game of Life as explained in the document statement. You can use the code skeleton provided here as a starting point. In that case, implement the `evolve` method in `gol.js`. Feel free to make changes to the code that help you capture all the rules of the game. You can add more tests to `golSpec.js` to verify the correctness of your code.

## Prerequisites ##

Your favorite editor, as well as `node` and `npm`- https://nodejs.org/

Once you have got them, run `npm install` in this directory

## Running Tests ##
### In node ###
`npm test`

#### Debugging ####
To run tests with a debugger, run the following then go to http://localhost:8282/debug?port=5858 in Chrome:

`npm install -g jasmine-node-debug`

`jasmine-node-debug`

Execution will initially be paused to allow you to add breakpoints.

### In the browser ###

`npm install -g webpack`

Then run: `npm run-script webpack-test` and open `_SpecRunner.html`

Every time you make a change you will have to run: `npm run-script webpack-test` and then refresh `_SpectRunner.html` in your browser window

#### Debugging #####
As you would in the browser normally, except all your output will be concatenated into a single file `bundle.js`
