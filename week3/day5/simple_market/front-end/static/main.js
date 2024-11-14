const getFarmersMarket = (info) => {
    let infoContainer = document.querySelector('#container')
    let marketDiv = document.createElement('div')
    marketDiv.style.border = "solid 2px black"
    infoContainer.appendChild(marketDiv)

    let para = document.createElement('p')

    para.textContent = info
    marketDiv.appendChild(para)
}

const getFarmersMarkets = async () => {
    const zipInput = document.querySelector('#zip-input');
    const distInput = document.querySelector('#distance-input')
    const zip = zipInput.value;
    const dist = distInput.value

    try {
        const response = await fetch(`https://www.usdalocalfoodportal.com/api/farmersmarket/?apikey=oIxGMeMXNe&zip=${zip}&radius=${dist}`)
        const markets = await response.json()
        console.log(markets)

        

        for (let i = 0; i < markets.data.length; i++){
            let name = markets.data[i].listing_name;
            let address = markets.data[i].location_address;
            let website = markets.data[i].media_website
            let distanceFrom = Math.floor(markets.data[i].distance)
            const marketInfo = `${name} is located at ${address}. It is about ${distanceFrom} miles from you.\nFind more info here: ${website}`
            console.log(marketInfo)
            getFarmersMarket(marketInfo)
        }

    } catch (error) {
        console.log(error)
    }
     
}