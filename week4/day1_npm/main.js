import axios from "axios"

const sayHello = ()=> {
    console.log("Hello")
}




const getPoke = () => {
    axios.get("https://pokeapi.co/api/v2/pokemon/ditto")
        .then((resp)=>{
            
            console.log(resp.data.sprites.front_default)
        })
}

getPoke()

// module.exports = {sayHello}