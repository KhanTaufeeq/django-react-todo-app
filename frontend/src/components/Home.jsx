import React from 'react';
import todo from '../assets/todo.jpeg';

function Home() {
    return (
        <>
            <div className="main-pic-div">
                <h1>The Only Todo App</h1>
                <img src={todo} alt="todo" id="todo-pic" />
            </div>
        </>
    )
}

export default Home;