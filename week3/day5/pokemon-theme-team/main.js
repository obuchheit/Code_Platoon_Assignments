console.log('Im connected')

const getPokeImg = (src) => {
    let imgContainer = document.querySelector("#container")
    let img = document.createElement('img')
    img.src = src
    img.style.width = '25vmin'
    img.style.height = '25vmin'
    img.style.border = 'solid 1px black'
    imgContainer.appendChild(img)
} 

//create a function that generates a random number between 1 and 1000 and then fetch poke data that corresponds to randInt
//Iterates through response to grab front_default sprite and then return front_default sprite

const getPokeFrontDefault = () =>{
    let num = Math.floor(Math.random()*1000)

    fetch(`https://pokeapi.co/api/v2/pokemon/${num}`)
        .then((response)=> response.json())
        .then((data)=>{
            //iterate through response to grab front_default
            let front_default = data.sprites.front_default

            //return front_default sprite

            getPokeImg(front_default)
        })
         .catch((error)=>{
            alert("something went wrong.")
        })
}


const getPokeFrontDefaultTwo = async () => {
    let num = Math.floor(Math.random()*1000)

    try {
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${num}`);
        const data = await response.json();
        console.log(data)        
        const typeUrl = data.types[0].type.url;
        console.log(typeUrl);

        const typeResponse = await fetch(typeUrl);
        const typeData = await typeResponse.json();
        console.log(typeData)

        let front_default = data.sprites.front_default

        getPokeImg(front_default)
    }   catch (error) {
        console.log('error')
    }
}


const getPokeTeam = async () => {
    let num = Math.floor(Math.random()*1000)

    try{
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${num}`);
        const data = await response.json();
        const typeUrl = data.types[0].type.url;
        console.log(typeUrl)
        const typeResponse = await fetch(typeUrl);
        const typeData = await typeResponse.json();

        let front_default = data.sprites.front_default

        getPokeImg(front_default)
        let pokeObj = {}
        pokeObj[num] = 'poke'
        console.log(pokeObj)
        
        for(let i = 0; i < 5; i++){
            const pokeNum = Math.floor(Math.random() * typeData.pokemon.length)
            console.log(pokeNum)
            const newPokeUrl = typeData.pokemon[pokeNum].pokemon.url
            console.log(typeData.pokemon)
            const pokeResponse = await fetch(newPokeUrl)
            const newPoke = await pokeResponse.json();
            console.log(newPokeUrl)
            const new_front_default = newPoke.sprites.front_default

            getPokeImg(new_front_default)
        }
        
    }   catch (error) {
        console.log('error')
    }    

}

