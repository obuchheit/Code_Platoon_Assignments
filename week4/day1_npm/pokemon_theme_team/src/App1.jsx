import { useState } from 'react'
import './App.css'
import axios from 'axios'


const [teamDiv, setTeamDiv] = useState(newDiv)
const [divId, setDivId] = useState(1)
const [characterImg, setCharacterImg] = useState(charImgs)

 
const getTeam = async() => {
    let randPoke = Math.floor(Math.random() * 1000)


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
