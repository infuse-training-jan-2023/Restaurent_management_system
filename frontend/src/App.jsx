import './App.css'
import Banner from './components/Banner'
import Footer from './components/Footer'
import Menutab from './components/Menutab'
import Reservation  from './components/TableReservation'
import Header from './components/Header'
import "./styles/output.css";

function App() {
  return (
    <div className="App">

            <Header/>
            <Banner/>
            <Menutab/>
            <Reservation/>
            <Footer/> 

    </div>
  )
}



export default App
