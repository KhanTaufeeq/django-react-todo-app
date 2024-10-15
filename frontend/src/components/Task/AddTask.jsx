import axios from "axios";
import React, { useState, useEffect } from "react";

function AddTask() {
  const [taskTitle, setTaskTitle] = useState("");
  const [taskBody, setTaskBody] = useState("");

  const csrftoken = document.cookie
  .split('; ')
  .find(row => row.startsWith('csrftoken='))
  ?.split('=')[1];  // Fetching CSRF token from cookie

  const addTaskFunction = () => {
    axios
      .post(
        "http://127.0.0.1:8000/task/add/",
        {
          title: taskTitle,
          body: taskBody,
        },
        {
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },
          withCredentials: true, // This ensures that cookies (including the session cookie) are sent
        }
      )
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
          <input
            type="text"
            name="title"
            id="title-input"
            placeholder="Title"
            onChange={(event) => setTaskTitle(event.target.value)}
          />
          <br />
          <input
            type="text"
            name="body"
            id="body-input"
            placeholder="Description"
            onChange={(event) => setTaskBody(event.target.value)}
          />
        </div>
        <button type="submit" onClick={addTaskFunction}>
          Add Your Task
        </button>
      </div>
    </>
  );
}

export default AddTask;
