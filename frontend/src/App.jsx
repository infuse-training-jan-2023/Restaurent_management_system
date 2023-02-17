import './App.css'
import { useState,useEffect } from 'react'
import Banner from './components/Banner'
import Footer from './components/Footer'
import Menutab from './components/Menutab'
import Header from './components/Header'
import {Context} from './context/CartContext'
import { AuthContext } from './context/AuthContext';
import ReserveTable from './components/TableReserve'

import "./styles/output.css";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  const storedUser = localStorage.getItem('user');
  const [user, setUser] = useState(JSON.parse(storedUser));

 useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }

  }, []);


  useEffect(() => {
    localStorage.setItem('user', JSON.stringify(user));
  }, [user]);

  const signIn = user => {
    setUser(user);
  };

  const signOut = () => {
    setUser(null);
  };

  const [context, setContext] = useState(localStorage.length);
  const [username, setUsername] = useState('');

  const scrollToBottom = () => {
    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: 'smooth',
    });
  };

  return (
    <>
      <AuthContext.Provider value={{ user, signIn, signOut }}>
        <Context.Provider value={[context, setContext]}>
          <div className="bg-orange-50">
            <Header/>
            <Banner scrollToBottom={scrollToBottom}/>
            <Menutab/>
            <ReserveTable/>
            <Footer/> 
          </div>
        </Context.Provider>
      </AuthContext.Provider>
    </>
  )
}



export default App
