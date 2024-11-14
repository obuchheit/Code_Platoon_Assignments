import { useState } from 'react'
import './App.css'





function App() {


  return (
    <>
      <div className='panel'>
          <span>Create a task: </span>
          <input type="text" placeholder='input task here' id='task-input'/>
          <input type="submit" id='submit'/>
      </div>
    </>
  )
}

export default App
