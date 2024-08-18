const holes = document.querySelectorAll('.hole');
const scoreBoard = document.querySelector('.score');
const moles = document.querySelectorAll('.mole');
const button = document.querySelector('#start');
let lastHole;
let timeUp = false;
let score = 0;

//randomTime(min, max): generates a random time interval between max and min millisceonds
function randomTime(min, max) {
	return Math.round(Math.random() * max - min) + min;
}

//randomHole(holes): randomly selects a hole from the list of holes and ensures the same hole does not appear consecutively
function randomHole(holes) {
	const index = Math.floor(Math.random() * holes.length);
	const hole = holes[index];

	if (hole === lastHole) {
		console.log('Same one as last');
		return randomHole(holes);
	}
	lastHole = hole;
	return hole;
}

//peep(): causes a mole to randomly pop up from a hole for a random amount of time
function peep() {
	const time = randomTime(200, 1000);
	const hole = randomHole(holes);
	hole.classList.add('up');
	setTimeout(() => {
		hole.classList.remove('up');
		if (!timeUp) peep();
	}, time);
}

//startGame(): resets the game state, hides start button, starts game by calling peep() function.
//              After a set amount of time(10 seconds), it ends the game and shows a button to "Try Again?"
function startGame() {
	scoreBoard.textContent = 0;
	timeUp = false;
	score = 0;
	button.style.visibility = 'hidden';
	peep();
	setTimeout(() => {
		timeUp = true;
		button.innerHTML = 'Try again?';
		button.style.visibility = 'visible';
	}, 10000);
}

//bonk(e): handles "whacking"/"bonking" of moles. When a mole is clicked, increments the score, updates the score display,
//         and removes the mole from view
function bonk(e) {
	if (!e.isTrusted) return;
	score++;
	this.classList.remove('up');
	scoreBoard.textContent = score;
}

moles.forEach((mole) => mole.addEventListener('click', bonk));
