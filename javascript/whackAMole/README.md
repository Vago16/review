# Whack A Mole

A simple interactive 10 second web browser game of whack a mole with a score that
increments everytime a mole is hit.

## How It's Made:

Tech used: HTML, CSS, JavaScript
Assets used in style: 'https://fonts.googleapis.com/css?family=Nunito',
'https://s3-us-west-2.amazonaws.com/s.cdpn.io/1159990/dirt.svg',
'https://s3-us-west-2.amazonaws.com/s.cdpn.io/1159990/mole.svg'

### Usage

1. Create an html doc with a class called "score" to house the number of moles hit later on and and a button with the id "start" and an onClick function titled "startGame()" that starts the game.

````html
<h2>Score: <span class="score">0</span></h2>
<button id="start" onclick="startGame()">Start</button>```
````

2. Include the script.js in the HTML doc containing the
   element with an id of "game" to house the majority of the interactive script.

```html
<div class="game">
	<div class="hole hole1">
		<div class="mole"></div>
	</div>
	<div class="hole hole2">
		<div class="mole"></div>
	</div>
	<div class="hole hole3">
		<div class="mole"></div>
	</div>
	<div class="hole hole4">
		<div class="mole"></div>
	</div>
	<div class="hole hole5">
		<div class="mole"></div>
	</div>
	<div class="hole hole6">
		<div class="mole"></div>
	</div>
</div>
```

3. In the javascript doc, write the startGame() function.

```javascript
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
```

4. After incorporating the other code, the game is ready to start. Just press the button to start and try to hit as many moles to get the highest score!
