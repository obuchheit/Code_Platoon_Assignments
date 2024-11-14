import { useState } from 'react'
import './App.css'
import axios from "axios"

function App() {
  //capture user input for desired poke name/id
  //make request for front sprite from pokeapi
  //render image for user
  //reset input field to blank

  const createImg = (url) => {
    let img = document.createElement("img")
    img.src = url
    img.style.height = "30vmin"
    img.style.width = "30vmin"
    img.style.border = "solid black 1px"
    document.getElementById('img-container').appendChild(img)
  }

  const getPokeImg = async(poke) => {
  try {
      let resp = await fetch(`https://pokeapi.co/api/v2/pokemon/${poke}`)
      let data = await resp.json()
      return data.sprites.front_default
    }
    
  
  catch(err){
    console.err(err)
    return null
    }
  }


  const handleSubmit = async(evt) => {
    evt.preventDefault()
    let finput = document.getElementById('user-input')
    let usrInput = finput.value
    let imgUrl = getPokeImg(usrInput)
    createImg(imgUrl)
    finput.value = ''
  }

  return (
    <>
      <form onSubmit={(evt) => handleSubmit(evt)}>
        <input id="user-input" type="text" placeholder='pokemon name'/>
        <input type="submit"/>
      </form>
      <div id='img-container'></div>
    </>
  )
}

export default App
