import { BrowserRouter, Routes, Route } from "react-router-dom"

import HomePage from "./pages/HomePage";
import CoursePage from "./pages/CoursePage";

function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route 
                    path="/" 
                    element={<HomePage />} 
                />

                <Route
                    path="/courses/:id"
                    element={<CoursePage />}
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;