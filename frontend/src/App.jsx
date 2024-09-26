import './App.css';
import Router from './Router';
import Home from './components/Home';

function App() {

  return (
    <>
      <div className="home-div">
        <Home/>
        <Router/>
      </div>
    </>
  )
}

export default App;