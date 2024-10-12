import axios from "axios";
import React, { useState, useEffect } from "react";

function AddTask() {
  const [taskTitle, setTaskTitle] = useState("");
  const [taskBody, setTaskBody] = useState("");

  const addTaskFunction = () => {
    axios
      .post("http://127.0.0.1:8000/task/add/", {
        title: taskTitle,
        body: taskBody,
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <>
      <div className="add-task-div">
        <div className="input-div">
          <input type="text" name="title" id="title-input" onChange={(event) => setTaskTitle(event.target.value)}/>
          <br />
          <input type="text" name="body" id="body-input" onChange={(event) => setTaskBody(event.target.value)}/>
        </div>
        <button type="submit" onClick={addTaskFunction}>Add Your Task</button>
      </div>
    </>
  );
}

export default AddTask;
