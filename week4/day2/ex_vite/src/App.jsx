import { useState, useEffect } from 'react'
import './App.css'
import jsontasks from "./tasks.json"
import axios from "axios"

function App() {

  // const [greeting, setGreeting] = useState('Hello')

  // const [tasks, setTasks] = useState(jsontasks)



  // const handleClick = () => {
  //   if (greeting === 'Hello') {
  //     setGreeting('Goodbye')
  //   }
  //   else{
  //     setGreeting('Hello')
  //   }
  // }

  // 2 params 1 = func, 2 = dependancy array
  // useEffect(()=>{
  //   console.log(greeting)
  // },[greeting])

  // const changeGreeting = () => {
  //   let h2 = document.getElementById('greeting') 
  //   if (h2.innerText === 'Hello') {
  //     h2.innerText = 'Goodbye'
  //   }
  //   else {
  //     h2.innerText = 'Hello'
      
  //   }
  // }
  const [characterImg, setCharacterImg] = useState("https://rickandmortyapi.com/api/character/1.jpeg")
  const [characterId, setCharacterId] = useState(1)

  const getCaracterImg = async() => {
    let {data} = await axios.get(`https://rickandmortyapi.com/api/character/${characterId}`)
    setCharacterImg(data.image)
  }

  useEffect(()=> {
    const getImg = async() =>{
      await getCaracterImg()
    }
    getImg()
  }, [characterId])

  return (
    <>
      <h1>Select a Character</h1>
      <img src={characterImg} />

      <button onClick={()=>setCharacterId(1)}>1</button>
      <button onClick={()=>setCharacterId(2)}>2</button>
      <button onClick={()=>setCharacterId(3)}>3</button>
      {/* <h1>{greeting} Owen</h1>
      <button onClick={handleClick}>update</button> */}

      {/* <h2 id='greeting'>{greeting}</h2> */}
      {/* <h2>{greeting}</h2>
      <button onClick={()=>setGreeting('Goodbye')}>Change Goodbye</button>
      <button onClick={()=>setGreeting('Hello')}>Change Hello</button>
       */}
      {/* <ul>
        {
          tasks.map((task)=>(
            <li>{task.task} <input type="radio" checked={task.completed} /></li>
          ))
        }
      </ul> */}
    </>
  )
}

export default App
