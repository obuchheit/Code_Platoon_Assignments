import { Link } from "react-router-dom"

function NavBar() {
    return (
        <div style={{backgroundColor: "lightblue"}}>
            <h1>NavBar</h1>
            <span>
                <Link to="/">Home Page</Link>
            </span>
            <span>
                <Link to="/about">About Page</Link>
            </span>
            <span>
                <Link to="/contact">Contact Us</Link>
            </span>
        </div>
        
    )
}

export default NavBar