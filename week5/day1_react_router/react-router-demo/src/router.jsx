import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import ContactPage from "./pages/ContactPage";
import ErrorPage from "./pages/ErrorPage";
import NotFound from "./pages/NotFound";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App/>,
        children: [
            {   
                index: true,
                element: <HomePage/>
            },
            {
                path: "about/",
                element: <AboutPage/>
            },
            {
                path: "contact/",
                element: <ContactPage/>
            },
            {
                path: "*",
                element: <NotFound/>
            }
        ],
        errorElement: <ErrorPage/>
    },

]);

export default router