describe("App.jsx", ()=>{
    it("visits baseUrl and checks for an h1 tag with Vite + React", ()=>{
        cy.visit('/')
        cy.get('h1').should('contain', "Vite + React")
    })
})