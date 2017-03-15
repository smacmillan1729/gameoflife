describe('Game', function (){
	var evolve = require('../script/gol')().evolve;

	it('can evolve an inital empty grid', function(){
		var initialState = [
			[0,0,0],
			[0,0,0],
			[0,0,0]
		];

		var resultState = [
			[0,0,0],
			[0,0,0],
			[0,0,0]
		];

		expect(evolve(initialState)).toEqual(resultState);
	});
});
