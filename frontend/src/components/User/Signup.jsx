import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Signup() {
    const [userName, setUserName] = useState('');
    const [email, setEmail] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [password, setPassword] = useState('');

    const userSignUp = (event) => {
        // Prevent form from submitting the traditional way
        event.preventDefault();

        axios.post('http://127.0.0.1:8000/user/signup/', {
        username: userName,
        first_name: firstName,
        last_name: lastName,
        email: email,
        password: password
    }, {
        headers:{
            'Content-Type': 'application/json'
        }
    })
    .then(res => {
        console.log(res);
    })
    .catch(err => {
        console.log(err);
    })
    }


    return (
        <div className="signup">
            <h2>Be a member!</h2>
            <form onSubmit={userSignUp}>
                <div className="text-div">
                    <label htmlFor="first_name">First Name</label>
                    <input type="text" name="first-name" id="first_name" value={firstName} onChange={(event) => setFirstName(event.target.value)} />
                </div>
                <div className="text-div">
                    <label htmlFor="last_name">Last Name</label>
                    <input type="text" name="last-name" id="last_name" value={lastName} onChange={(event) => setLastName(event.target.value)} />
                </div>
                <div className="text-div">
                    <label htmlFor="username">Username</label>
                    <input type="text" name="username" placeholder='Enter your username' id="username" value = {userName} onChange={(event) => setUserName(event.target.value)} />
                </div>
                <div className="text-div">
                    <label htmlFor="email">Email</label>
                    <input type="email" name="email" id="email" placeholder="Enter your email" value = {email} onChange={(event) => setEmail(event.target.value)} />
                </div>
                <div className="text-div">
                    <label htmlFor="password">Password</label>
                    <input type="password" name="password" id="password" placeholder="Password" value = {password} onChange={(event) => setPassword(event.target.value)} />
                </div>
                <button type="submit">Register</button>
            </form>
            <Link to="/">Already a member?</Link>
        </div>
    )
}

export default Signup;