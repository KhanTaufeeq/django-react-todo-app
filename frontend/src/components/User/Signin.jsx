import React, { useState } from "react";
import { Link, json } from "react-router-dom";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Home from "../Home";

function Signin() {

  const [userSigninName, setUserSigninName] = useState('')
  const [userSigninPassword, setUserSigninPassword] = useState('')
  const [userId, setUserId] = useState(null);
  const navigate = useNavigate();
  

  const userSignIn = (event) => {
    console.log('submitting form');
    event.preventDefault();
    axios.post('http://127.0.0.1:8000/user/signin/', {
      "username": userSigninName,
      "password": userSigninPassword
    },
      {
        headers: {
          'Content-Type': 'application/json'
        },
        withCredentials: true
      }
    )
      .then(res => {
        console.log(res.data.user_id);
        console.log('signin response: ', userSigninName);
        localStorage.setItem('user_id', JSON.stringify(res.data.user_id));
        setUserId(res.data.user_id);
        navigate('mytask');
      })
      .catch(err => {
        console.log(err);
      });
  }

  // React's useState updates the state asynchronously, 
  // meaning that userId may not yet be updated by the time localStorage.setItem('user_id', JSON.stringify(userId)) is called. 
  // At that moment, userId may still be null.

  // const routeToHomeTask = () => {
  //   console.log(userSigninName);
  //   console.log(userSigninPassword);
  //   navigate('mytask');
  // }


  return (
    <>
    <Home/>
      <div className="signin-div">
        <h2>Let's Schedule</h2>
        <div className="input-div">
          <form onSubmit={userSignIn}>
            <div className="username-div">
              <label htmlFor="username">Username</label>
              <input type="text" name="username" id="username" onChange={(event) => setUserSigninName(event.target.value)}/>
            </div>
            <div className="password-div">
              <label htmlFor="password">Password</label>
              <input type="password" name="password" id="password" onChange={(event) => setUserSigninPassword(event.target.value)}/>
            </div>
            <br />
            <button type="submit">Login</button>
          </form>
        </div>
        <Link to="/signup">Not a member?</Link>
      </div>
    </>
  );
}

export default Signin;
