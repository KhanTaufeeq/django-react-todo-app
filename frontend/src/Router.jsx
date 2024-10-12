import Signup from "./components/User/Signup";
import Signin from "./components/User/Signin";
import { Routes, Route } from "react-router-dom";
import TaskHome from "./components/Task/TaskHome";

const Router = () => {
    return (
        <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/" element={<Signin />} />
            <Route path="/mytask" element={<TaskHome />} />
        </Routes>
    )
}

export default Router;