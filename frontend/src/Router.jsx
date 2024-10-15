import Signup from "./components/User/Signup";
import Signin from "./components/User/Signin";
import { Routes, Route } from "react-router-dom";
import TaskHome from "./components/Task/TaskHome";
import AddTask from "./components/Task/AddTask";

const Router = () => {
    return (
        <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/" element={<Signin />} />
            <Route path="/mytask" element={<TaskHome />} />
            <Route path = "/addtask" element={<AddTask/>} />
        </Routes>
    )
}

export default Router;