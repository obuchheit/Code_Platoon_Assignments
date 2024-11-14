import { useState } from 'react'
import { useEffect } from 'react';
import Form from 'react-bootstrap/Form';
import Button from "react-bootstrap/Button";
import PokeCards from './components/PokeCard';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css'
import axios from 'axios';



function App() {
  const [type, setType] = useState("")
  const [pokemon, setPokemon] = useState([])
  const [ishidden, setIsHidden] = useState(true)



  const makeType = async(e) => {
    e.preventDefault()
    console.log(type)

    let { data } = await axios.get(`https://pokeapi.co/api/v2/type/${type}`)
    console.log(data)

    for(let i = 0; i < 6; i++) {
      let randNum = Math.floor(Math.random() * data.pokemon.length)
      let pokeurl = data.pokemon[randNum].pokemon.url

      setPokemon(currentPokemon => {
        return [...currentPokemon, pokeurl]
      })
    }
    setIsHidden(false)
  }

 



  return (
    <>
    
    <h1 className='mb-4'>Pokemon Theme Team</h1>
    <div className='form-container'>
      <Form onSubmit={(e) => makeType(e)}>
        <div>
          <Form.Select className='mb-12 drop' onChange={(e)=> setType(e.target.value)}>
            <option>Select Your Pokemon Type</option>
            <option value="1">Normal</option>
            <option value="2">Fighting</option>
            <option value="3">Flying</option>
            <option value="4">Poison</option>
            <option value="5">Ground</option>
            <option value="6">Rock</option>
            <option value="7">Bug</option>
            <option value="8">Ghost</option>
            <option value="9">Steel</option>
            <option value="10">Fire</option>
            <option value="11">Water</option>
            <option value="12">Grass</option>
            <option value="13">Electric</option>
            <option value="14">Psychic</option>
            <option value="15">Ice</option>
            <option value="16">Dragon</option>
            <option value="17">Dark</option>
            <option value="18">Fairy</option>
          </Form.Select>
          <div className='button-container'>
          <Button
          className='subButton'
          variant='primary'
          type='submit'
          size='xxl'
          >Create Team</Button>
        </div>
        </div>
      </Form>
    </div>
    

    <PokeCards pokemon={pokemon} show={ishidden}/>
    </>
  )
}

export default App
