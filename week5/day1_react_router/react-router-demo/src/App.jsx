import { Outlet } from 'react-router-dom'
import { useState, useEffect } from 'react'
import NavBar from './components/NavBar'
import './App.css'

function App() {

  return (
    <>
      <NavBar/>
      <Outlet/>
    </>
  )
}

export default App
