import React from "react";
import { useState,useEffect } from "react";
import logo from '../assets/logo.jpg';
import axios from 'axios'
import DatePicker from "react-datepicker";
import TimePicker from "react-time-picker";

import "react-datepicker/dist/react-datepicker.css";
const Reservation =()=>
{   
    const fetchData = async () => {
        axios.get('http://localhost:8000/tables')
          .then(res => {
            setTable(res.data)
            console.log(res.data);
          })
      };  

      useEffect(() => {
        fetchData()
      },[]);
      const [tables ,setTable] = useState([])
     
    const date = new Date()
    const [reserveDate, setReserveDate] = useState(date)
    const [fromTime, onChange] = useState('10:00');
    const [toTime, changeTime] = useState('11:00');

    const tomorrow = new Date()
    return(
    <section className="my-12 max-w-screen-xl mx-auto px-6">
      <div className="items-center text-center justify-center">
          <DatePicker className="border-primary text-center bg-white py-3 px-3 rounded-full text-black"
            selected={reserveDate}
            selectsStart
            dateFormat="dd/MM/yyyy"
            onChange={date => setReserveDate(date)}
            includeDates ={[date,tomorrow.setDate(date. getDate() + 1),tomorrow.setDate(date. getDate() + 2) ]}
          />
          
          From: <TimePicker className="mx-4 mt-4"        
          minTime={new Date(0, 0, 0, 8)}
          maxTime={new Date(0, 0, 0, 18, 45)}
          onChange={onChange} value={fromTime} /> 
          To: <TimePicker onChange={changeTime}
          minTime={new Date(0, 0, 0, 8)}
          maxTime={new Date(0, 0, 0, 18, 45)}
          value={toTime} />
      </div>

        
      
          <div class="grid grid-cols-5 text-center gap-2 mt-5">
                {
                  tables.map((table)=>
                  (<TableCard capicity={"/table"+table.capicity+".svg"} status={table.available} > 
                  </TableCard>
                  )
                   
              )
                  
              }
            </div>                
    </section>)
}

const addEntry = (val) =>{
    if(val){
      axios.post('http://localhost:8000/tables',{
        date: reserveDate,
        from_time: fromTime,
        to_time: toTime,
        available:false
      })
          .then(res => {
            console.log(res.data);
          })
    }
}

const TableCard = (props) => { 
  console.log(props.status)
    let classval = "h-15 w-15 "
    if (props.status)
      classval+="bg-green-300"
    else
      classval +="bg-red-300" 
    console.log(classval)
    return (
           <img src={props.capicity} onClick={addEntry(props.status)} className={classval} />  
    )
} 



export default Reservation