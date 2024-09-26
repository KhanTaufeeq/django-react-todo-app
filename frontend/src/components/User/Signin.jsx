import React from "react";
import { Link } from "react-router-dom";

function Signin() {
  return (
    <>
      <div className="signin-div">
        <h2>Let's Schedule</h2>
        <div className="input-div">
          <form action="">
            <div className="username-div">
              <label htmlFor="username">Username</label>
              <input type="text" name="username" id="username" />
            </div>
            <div className="password-div">
              <label htmlFor="password">Password</label>
              <input type="password" name="password" id="password" />
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
