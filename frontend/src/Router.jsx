import Signup from "./components/User/Signup";
import Signin from "./components/User/Signin";
import { Routes, Route } from "react-router-dom";

const Router = () => {
    return (
        <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/" element={<Signin />} />
        </Routes>
    )
}

export default Router;