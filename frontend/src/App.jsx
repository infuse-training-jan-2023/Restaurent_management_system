import './App.css'
import Banner from './components/Banner'
import Footer from './components/Footer'
import Menutab from './components/Menutab'
import Header from './components/Header'
import Feedback from './components/feedback'
import Cart from './components/Cart'
import "./styles/output.css";

function App() {
  return (
    <div className="App">

            <Header/>
            <Banner/>
            <Menutab/>
            <Footer/> 
            <Feedback/>

    </div>
  )
}



export default App
