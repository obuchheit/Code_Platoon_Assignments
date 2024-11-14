import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [microphone, setMicro] = useState("../icons/on.svg")

  const changeMic = () => {
    if (microphone === "../icons/on.svg") {
      setMicro("../icons/off.svg")
    }
    else {
      setMicro("../icons/on.svg")
    }
  }

  return (
    <>
      <img src={microphone} id='mic' onClick={changeMic}/>
    </>
  )
}

export default App
