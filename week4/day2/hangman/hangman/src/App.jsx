import { useState } from 'react'
import { useEffect } from 'react';
import './App.css'
import words from './data/data.json'

function App() {

  const [answer, setAnswer] = useState("");
  const [guess, setGuess] = useState("")
  const [displayword, setDisplayWord] = useState("")
  const [guessedLetters, setGuessedLetters] = useState([])
  const [correctLetters, setCorrectLetters] = useState([])
  const [lives, setLives] = useState(5)

  
  const newGuess = (e) => {
    e.preventDefault()
    if (answer.includes(guess)) {
      setCorrectLetters(currentCorrectLetters => {
        return [...currentCorrectLetters, guess]
      })

      setDisplayWord(encodeDisplayWord)
    }

    else {
      setGuessedLetters(currentGuessedLetters =>{
        return [...currentGuessedLetters, guess + ", "]
      })
      setLives(lives - 1)
    }

    setGuess("")
  }



  const compareLettersToAnswer = (letter) => {
    if (correctLetters.includes(letter.toLowerCase())) {
      return letter
    }
    else {
      return "_ "
    }
  }  

  const encodeDisplayWord = () => {
    const disArr = answer.split("").map(compareLettersToAnswer)
    return disArr.join("")
  }



// Start Game Vars
  const startGame = () => {
    setAnswer(words[Math.floor(Math.random() * words.length +1)])
    encodeDisplayWord()
  }


  useEffect(() => {
    setDisplayWord(encodeDisplayWord());
  });
 

  return (
    <>
      <h1>Hangman</h1>

      <button onClick={startGame}>Start Game</button>
      
      <h2>{displayword}</h2>

      <h3>Lives left: {lives}</h3>
      
      <form onSubmit={e => newGuess(e)}>
        <input type="text"
          maxLength={1}
          value={guess}
          onChange={(e) => setGuess(e.target.value)}/>
        <input type="submit" />
      </form>

      <h3>Guessed Letters: {guessedLetters}</h3>

    </>
  )
}

export default App
