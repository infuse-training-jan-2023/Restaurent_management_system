import React from "react";
import axios from 'axios'
import { useState,useContext} from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";



const ReserveTable = () =>{
  

  const date = new Date();
  const tomorrow = new Date();
  const [reservationData ,setReservationData]= useState([])
  const [reservationDate ,setReservationDate]= useState(date)
  const [slot ,setSlot]= useState('Morning')

  axios.get('http://localhost:8000/tables')
  .then(res => {
    setReservationData(res.data.data)
  })
  .catch(error => {
    console.error(error);
  });

  const tableData = [
    { table_no: 1, capacity: 2, price: 5000 },
    { table_no: 2, capacity: 2, price: 5000 },
    { table_no: 3, capacity: 2, price: 5000 },
    { table_no: 4, capacity: 4, price: 10000 },
    { table_no: 5, capacity: 4, price: 10000 },
    { table_no: 6, capacity: 4, price: 10000 },
    { table_no: 7, capacity: 8, price: 12000 },
    { table_no: 8, capacity: 8, price: 12000 },
    { table_no: 9, capacity: 8, price: 12000 },
  ];
  console.log(reservationDate)
  console.log(slot)
  const reserved = []
  const formatDate = (Rdate) => {
    let dd = Rdate.getDate();
    let mm = Rdate.getMonth() + 1;
    let yyyy = Rdate.getFullYear();
    if (dd < 10) dd = "0" + dd;
    if (mm < 10) mm = "0" + mm;
    let udate = dd + "-" + mm + "-" + yyyy;
    return udate;
  };

  // const userName = "Dummy"
  //   const reserveData = {
  //     user_name: userName , 
  //     table_no: tableNo,
  //     capacity: tableCapacity,
  //     date: reserveDate,
  //     price: tablePrice,
  //     slot: slot
  //     }
  
  // const reserve_table =  () =>{
  //   console.log("inside");
  //   axios.post("http://localhost:8000/tables",reserveData).then((res) => {
  //   console.log("done")
  //   console.log(res.data);
  //   alert("Table has been reserved successfully")
  // }).catch(error => { console.log(error); });
  // }
  const updateUI = (value, update) => {
    reserved.splice(0, reserved.length)
    if (value) setReservationDate(update);
    else setSlot(update);
    reservationData.map((data) => {
      console.log("Outside"+ data.slot + slot +reservationDate +  data.date )
      if (slot == data.slot && reservationDate == formatDate(data.date))
      console.log("Data"+ data.slot + slot +reservationDate +  data.date )
        reserved.push(data.table_no);
    });
  };

  const getBgColor = (val) => {
    console.log(reserved)
    if (reserved.length > 0) {
      reserved.map((r) => {
        if (r.table_no == val){ 
          console.warn("r" + r.table_no + " val "+val )
          return (style = "bg-gray-400");
      }
      });
    }
    return " ";
  };

  const TableCard = (props) => {    

      return (
        <div className="inline-block  px-2 w-84 ">
          <div className="w-96 h-40 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-2xl transition-shadow  duration-300 ease-in-out ">
            <h1 className="text-gray-900 text-center poppins text-lg">
              Table No: {props.data.table_no}
            </h1>
            <img
              src={"table" + props.data.capacity + ".svg"}
              className={ getBgColor(props.data.table_no)+ " w-36 h-20 mx-auto "}
            /> 
            {/* onClick={()=>loadModal(props.styles[0],props.data)} to be inserted inside image */}
            <span className="text-gray-900 ml-2 text-left poppins text-lg">
              Capacity: {props.data.capacity}
            </span>
            <span className="text-gray-900 ml-24 poppins text-xl font-semibold">
              &#8377;{props.data.price}
            </span>
          </div>
        </div>
      );
  
  };

  //const [tableNo, setTableNumber] = useState();
  //const [tablePrice,setPrice] =useState();
  //const [tableCapacity,setCapacity] =useState();
  //const [isShown, setIsShown] = useState(false);
  /*const loadModal = (val, data) => {
    if (!val) {
      console.log(data);
      setIsShown(true);
      setPrice(data.price);
      setTableNumber(data.table_no);
      setCapacity(data.capicity);
    }
  };
  */
  


  return (
    <section className="bg-orange-50 my-12 py-10   max-w-screen-xl mx-auto px-6">
      <div className="text-center ml-auto mr-auto w-max ">
        <DatePicker
          className=" static text-center w-2/5 "
          portalId="root-portal"
          selected={reservationDate}
          selectsStart
          dateFormat="dd/MM/yyyy"
          onChange={(date) => updateUI(true, date)}
          includeDates={[
            date,
            tomorrow.setDate(date.getDate() + 1),
            tomorrow.setDate(date.getDate() + 2),
          ]}
        />
        <span>
          <label className="p-2">Select slot:</label>
          <select onChange={(e) => updateUI(false, e.target.value)}>
            <option value="Morning">Morning</option>
            <option value="Afternoon">Afternoon</option>
            <option value="Evening">Evening</option>
          </select>
        </span>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-20 overflow-y-scroll h-96">
        {tableData.map((table) => (
          <TableCard
            data = {table}
          ></TableCard>
        ))}
      </div>

      {/* {isShown &&       
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
                  <button type="button" onClick={reserve_table} className="bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                    Confirm
                  </button>
                  <button type="button" onClick={show_login_modal} className="text-sm font-medium text-teal-500 hover:text-teal-400">
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
    </div>
      } */}
    </section>
  );
    
          

}
export default ReserveTable