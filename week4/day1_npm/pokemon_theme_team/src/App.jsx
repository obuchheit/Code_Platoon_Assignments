import { useState } from 'react'
import './App.css'
import axios from 'axios'

let counter = 0;

const makeImg = (src) => {
  let imgContainer = document.querySelector(`#team-container${counter}`)
  let img = document.createElement('img')
  img.src = src
  img.className = 'poke-image'
  document.getElementById(`team-container${counter}`).appendChild(img)
}

const makeTeam = async (evt) => {
  counter += 1
  const teamContainer = document.querySelector('root')
  const container = document.createElement('div')
  container.id = `team-container${counter}`
  container.className = "team-cont"
  document.getElementById("root").appendChild(container)
  let num = Math.floor(Math.random()*1000)
  let resp = await axios.get(`https://pokeapi.co/api/v2/pokemon/${num}`)
  let data = resp.data;
  let imgUrl = data.sprites.front_default;

  let type = await data.types[0].type.url;
  let typeResp = await axios.get(type);
  let typeData = typeResp.data;


  makeImg(imgUrl)

  let used_dict = {}

  for(let i = 0; i < 5; i++) {
    const pokeNum = Math.floor(Math.random() * typeData.pokemon.length)
    const newPokeUrl = typeData.pokemon[pokeNum].pokemon.url
    const pokeResponse = await fetch(newPokeUrl)
    const newPoke = await pokeResponse.json();
    const new_front_default = newPoke.sprites.front_default

    makeImg(new_front_default)
}

}

function App() {

  return (
    <>
      <div id='panel'>
        <span>Create Team: </span>
        <button id="create-button" onClick={(evt)=>makeTeam(evt)}>Create</button>
      </div>
    </>
  )
}

export default App
