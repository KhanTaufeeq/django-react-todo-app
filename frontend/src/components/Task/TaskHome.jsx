import axios from 'axios';
import React, {useState, useEffect} from 'react';
import plus from '../../assets/plus.png';
import AddTask from './AddTask';
import { useParams } from 'react-router';
import { useNavigate } from 'react-router';
import '../../App.css';


function TaskHome() {
  const {userId} = useParams();
  const [taskList, setTaskList] = useState([]);
  const navigate = useNavigate();

  let getUserId = JSON.parse(localStorage.getItem('user_id'));


  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/task/${getUserId}/`)
    .then((res) => {
      console.log(res);
      setTaskList(res.data.tasks);
    })
    .catch((error) => {
      console.log(error);
    })
  }, []);

  return (
    <>
    <h1>Your all tasks are here</h1>
    <img src={plus} alt="add-task" onClick={() => navigate('/addtask')} id="plus-img"/>
    <div className="tasks-list-div">
      {
        taskList.map(task => (
          <>
          <h2 key={task.id}>
            {task.title}
          </h2>
          <p>{task.body}</p>
          </>
        ))
      }
    </div>
    </>
  )
}

export default TaskHome;