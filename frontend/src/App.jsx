import './App.css'
import Banner from './components/Banner'
import Footer from './components/Footer'
import Menutab from './components/Menutab'
import Navbar from './components/Navbar'
import Table  from './components/Table'

import "./styles/output.css";


function App() {
  return (
    <div className="App">
            <Navbar/>
            <Banner/>
            <Menutab/>
            <Table/>
            <Footer/> 

    </div>
  )
}



export default App
