
let correctNum = Math.floor(Math.random() * 100);
console.log(correctNum)


document.getElementById('guess-input').addEventListener('submit', function(event) {
    event.preventDefault()
    let currentGuess = document.getElementById('guess-input').value;
    console.log(currentGuess)

})

function newGame(evt) {
    location.reload
}