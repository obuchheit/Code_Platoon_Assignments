import exp from "constants"
import sayHello from "./main.js"

const {sayHello} = require("./main.js")

it("should return true", ()=>{
    expect(true).toBe(true)
})

it("ensure sayHello was inported properly", ()=>{
    expect(sayHello()).toBe("Hello")
})