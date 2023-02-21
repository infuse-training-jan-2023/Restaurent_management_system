import React from "react";
import axios from "axios";
import { useState, useEffect,useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { message } from "antd";

const ReserveTable = () => {
  const date = new Date();
  const tomorrow = new Date();
  const [reservationData, setReservationData] = useState([]);
  const [reservationDate, setReservationDate] = useState(date);
  const [slot, setSlot] = useState("Morning");
  const {user} = useContext(AuthContext);

  const info = () => {
    if (user){} 
    else message.warning("user not logged");
  };


  const getdata = () => {
    axios
      .get("http://localhost:8000/tables")
      .then((res) => {
        setReservationData(res.data.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

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
  const reserved = [];

  const reserve_table = () => {
    axios
      .post("http://localhost:8000/tables", reserveData)
      .then((res) => {
        message.success("Table has been reserved successfully");
        show_modal();
        getdata();
      })
      .catch((error) => {
        console.log(error);
      });
  };
  const getBgColor = (val) => {
    reserved.splice(0, reserved.length);
    if (reservationData != null) {
      reservationData.map((data) => {
        if (slot == data.slot) {
          if (
            reservationDate.toISOString().substring(0, 10) ==
            data.date.substring(0, 10)
          ) {
            reserved.push(data.table_no);
          }
        }
      });
    }

    let x;
    if (reserved.length > 0) {
      x = reserved.map((r) => {
        if (r == val) {
          return true;
        } else return false;
      });
    }

    return x;
  };

  useEffect(() => {
    getdata();
  }, [slot]);

  const TableCard = (props) => {
    var val = getBgColor(props.data.table_no);
    var style = " ";
    var flag = 0;
    if (val != undefined) {
      if (val.includes(true)) {
        style = "bg-red-100 ";
        flag = 1;
      }
    }
    return (
      <div className="inline-block px-2 w-84 custom_table_card">
        <div
          className={
            style +
            "w-96 h-40 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-2xl transition-shadow  duration-300 ease-in-out "
          }
          onClick={() => {info(); console.log(user); if(user != null) loadModal(props.data, flag);}}
        >
          <h1 className="text-gray-900 text-center poppins text-lg">
            Table No: {props.data.table_no}
          </h1>
          <img
            src={"table" + props.data.capacity + ".svg"}
            className=" w-36 h-20 mx-auto "
          />
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

  const [tableNo, setTableNumber] = useState();
  const [tablePrice, setPrice] = useState();
  const [tableCapacity, setCapacity] = useState();
  const [isShown, setIsShown] = useState(false);
  const loadModal = (data, flag) => {
    if (!flag == 1) {
      setIsShown(true);
      setPrice(data.price);
      setTableNumber(data.table_no);
      setCapacity(data.capacity);
    } else message.warning("Table already Reserved !!!");
  };
  const reserveData = {
    user_name: user,
    table_no: tableNo,
    capacity: tableCapacity,
    price: tablePrice,
    date: reservationDate,
    slot: slot,
  };
 
  const show_modal = () => {
    setIsShown((current) => !current);
  };

  return (
    <section className="bg-orange-50 my-12 py-10 max-w-screen-xl mx-auto px-6 custom_tablereserve_header">
      <div>
        <h1 className="text-center text-4xl">Table Reservation</h1>
      </div>
      <div className="text-center ml-auto mr-auto w-max flex mt-2">
        <div className="rounded-full box-border bg-white border border-black overflow-hidden flex items-center p-1 mr-2 custom_tablecss">
          <label className="p-1 py-3 pl-3 text-sm bg-primary px-6 rounded-full text-white poppins ring-red-300 focus:ring-4 transition duration-300 hover:scale-105 custom_label">
            Select Date:
          </label>
          <DatePicker
            className="text-center w-28 p-1 py-2 rounded-full focus:outline-none border-solid border-black bg-transparent"
            portalId="root-portal"
            selected={reservationDate}
            selectsStart
            dateFormat="dd/MM/yyyy"
            onChange={(date) => setReservationDate(date)}
            includeDates={[
              date,
              tomorrow.setDate(date.getDate() + 1),
              tomorrow.setDate(date.getDate() + 2),
            ]}
          />
        </div>
        <div className="ml-5 custom_tablecss">
          <span className="rounded-full box-border bg-white border border-black overflow-hidden flex items-center p-1">
            <label className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-red-300 focus:ring-4 transition duration-300 hover:scale-105 custom_label">
              Select slot:
            </label>
            <select
              className="text-center w-28 p-1 py-2 rounded-full focus:outline-none border-solid border-black bg-transparent"
              onChange={(e) => setSlot(e.target.value)}
            >
              <option value="Morning">Morning</option>
              <option value="Afternoon">Afternoon</option>
              <option value="Evening">Evening</option>
            </select>
          </span>
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-20 overflow-y-scroll h-96">
        {tableData.map((table) => (
          <TableCard data={table}></TableCard>
        ))}
      </div>

      {isShown && (
        <div className="relative">
          <div className="fixed top-0 left-0 right-0 bottom-0 opacity-100 bg-opacity-60 bg-black z-50">
            <div className="flex items-center justify-center h-full mx-auto">
              <div className="bg-white p-16 rounded-lg shadow-xl">
                <form className="text-center">
                  <h2 className="text-lg font-medium mb-6">Reserve Table </h2>
                  <div className="mb-5">
                    <label className="block mb-2 text-md font-medium text-black-0">
                      Reserve Table : {tableNo}
                    </label>
                  </div>
                  <div className="mb-6">
                    <label className="block mb-2 text-md font-medium text-black">
                      Price : {tablePrice}
                    </label>
                  </div>
                  <div className="flex items-center justify-between">
                    <button
                      type="button"
                      onClick={reserve_table}
                      className="bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-4 rounded focus:outline-none focus:shadow-outline mr-2"
                    >
                      Confirm
                    </button>
                    <button
                      type="button"
                      onClick={show_modal}
                      className="text-sm font-medium text-teal-500 hover:text-teal-400"
                    >
                      Cancel
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      )}
    </section>
  );
};
export default ReserveTable;
