import React from "react";
import { useState, useEffect } from "react";
import logo from "../assets/logo.jpg";
import axios from "axios";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";
const Reservation = () => {
  const fetchData = async () => {
    axios.get("http://localhost:8000/tables").then((res) => {
      setTable(res.data);

      console.log(res.data);
    });
  };
   const [isShown, setIsShown] = useState(false);
  
    const show_login_modal = () => {
  
      setIsShown(current => !current);
    };

    

  useEffect(() => {
    fetchData();
  }, []);
  const [tables, setTable] = useState([]);
  const [slot, setSlot] = useState([]);
  const [reserve, setReservation] = useState([tables]);
  const [tableNo, setTableNumber] = useState();
  const [tablePrice,setPrice] =useState();
  const [tableCapacity,setCapacity] =useState();
  const date = new Date();
  const [reserveDate, setReserveDate] = useState(date);
  const [open, setOpen] = useState(false);

  const handleOpen = () => {
    console.log(open);
    setOpen((current) => !current);
  };
  const userName = "Dummy"
  const reserveData = {
    user_name: userName , 
    table_no: tableNo,
    capicity: tableCapacity,
    date: reserveDate,
    price: tablePrice,
    slot: slot
    }
  const reserve_table = async () =>{
    axios.post("http://localhost:8000/tables",reserveData).then((res) => {
    console.log("done")
    console.log(res.data);
  }).catch(error => { console.error(error); });
  }


  const tableData = [
    { table_no: 1, capicity: 2, price: 5000 },
    { table_no: 2, capicity: 2, price: 5000 },
    { table_no: 3, capicity: 4, price: 10000 },
    { table_no: 4, capicity: 4, price: 10000 },
    { table_no: 5, capicity: 8, price: 12000 },
    { table_no: 6, capicity: 8, price: 12000 },
  ];
  const checkTable = (slot) => {
    setSlot(slot)
    var reservationEntry = [];
    setReservation(
      tables.filter((data) => {
        if (data.slot == slot && data.date == gfg_Run(reserveDate)) {
          tableData.map((tab) => {
            if (tab.table_no == data.table_no)
              reservationEntry.push(tab.table_no);
          });
          console.warn(reservationEntry);
          return reservationEntry;
        }
      })
    );
  };

  const gfg_Run = (Rdate) => {
    var date = Rdate.toJSON().slice(0, 10);
    var nDate =
      date.slice(8, 10) + "-" + date.slice(5, 7) + "-" + date.slice(0, 4);
    return nDate;
  };

  const loadModal = (val,data)=>{
    if(!val){
      console.log(data)
      setIsShown(true)
      setPrice(data.price)
      setTableNumber(data.table_no)
      setCapacity(data.capicity)
    }
  };
  
  const TableCard = (props) => {
    console.log(props);
    var style = "h-15 w-15 "
    if(props.styles[0])
      style="h-15 w-15 bg-gray-400"
    return <img src={props.capicity} className={style} onClick={()=>loadModal(props.styles[0],props.data)} />;
  };



  const tomorrow = new Date();
  return (
    <section className="">
      <DatePicker
        selected={reserveDate}
        selectsStart
        dateFormat="dd/MM/yyyy"
        onChange={(date) => setReserveDate(date)}
        includeDates={[
          date,
          tomorrow.setDate(date.getDate() + 1),
          tomorrow.setDate(date.getDate() + 2),
        ]}
      />

      <button
        className="border-primary  rounded-md text-sm mt-4 text-center bg-primary py-1 px-1  text-white"
        onClick={handleOpen}
      >
        Select Slot :{" "}
      </button>
      {open && (
        <ul className="menu text-sm border-primary mr-auto ml-auto mt-1 bg-white w-20 text-black">
          <li className="menu-item  text-sm hover:bg-red-200">
            <button onClick={() => checkTable("Morning")}>Morning</button>
          </li>
          <li className="menu-item text-sm hover:bg-red-200">
            <button onClick={() => checkTable("Afternoon")}>Afternoon</button>
          </li>
          <li className="menu-item text-sm hover:bg-red-200">
            <button onClick={() => checkTable("Evening")}>Evening </button>
          </li>
        </ul>
      )}

      <div className="grid grid-cols-6 text-center gap-2 mt-5">
        {tableData.map((table) => (
          <>
            {reserve.forEach((r) =>
              r.table_no == table.table_no
                ? "h-15 w-15 bg-gray-200"
                : "h-15 w-15"
            )}

            <TableCard
              capicity={"/table" + table.capicity + ".svg"} data={table}
              styles={ reserve.map(r => (r.table_no == table.table_no) ? true : false)}
            ></TableCard>
          </>
        ))}
      </div>

      {isShown &&       
      <div className="relative">
        <div className="fixed top-0 left-0 right-0 bottom-0 opacity-100 bg-black z-50">
          <div className="flex items-center justify-center h-full mx-auto">
            <div className="bg-white p-16 rounded-lg shadow-xl">
              <form className="text-center">
                <h2 className="text-lg font-medium mb-6">Reserve Table </h2>
                <div className="mb-5">
                  <label className="block mb-2 text-sm font-medium text-black-0">
                    Reserve Table : {tableNo}
                  </label>
                </div>
                <div className="mb-6">
                  <label className="block mb-2 text-sm font-medium text-black">
                    Price : {tablePrice}
                  </label>
                </div>
                <div className="flex items-center justify-between">
                  <button onClick={reserve_table} className="bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                    Confirm
                  </button>
                  <button onClick={show_login_modal} className="text-sm font-medium text-teal-500 hover:text-teal-400">
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
    </div>
      }

    </section>
  );
};


export default Reservation;
