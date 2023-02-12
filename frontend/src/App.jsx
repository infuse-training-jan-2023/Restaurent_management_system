import './App.css'
import { useState } from 'react'
import Banner from './components/Banner'
import Footer from './components/Footer'
import Menutab from './components/Menutab'
import Header from './components/Header'
import {Context} from './context/usercontext copy'
import { Username } from './context/username'
import "./styles/output.css";

function App() {
  const [context, setContext] = useState(localStorage.length);
  const [username, setUsername] = useState('');
  return (
    <Username.Provider value={[username,setUsername]}>
    <Context.Provider value={[context, setContext]}>
    <div className="App">

            <Header/>
            <Banner/>
            <Menutab/>
            <Footer/>

    </div>
    </Context.Provider>
    </Username.Provider>
  )
}



export default App
