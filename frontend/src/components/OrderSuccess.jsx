import React from "react";
import { useState,useEffect,useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { Result } from "antd";
import axios from "axios";

const OrderMsg = ({ onClick }) => {
  const [orderConfirm, setOrderConfirmation]=useState('')
  const [confirmModal, setConfirmationModal]=useState(true)
  const { user, signIn, signOut } = useContext(AuthContext);

  const [total, settotal] =useState('')
  useEffect(() => {
      axios
        .get(`http://localhost:8000/cart/${user}`)
        .then((res) => {
          settotal(res.data.data.grand_total);
        })
        .catch((error) => {
          console.error(error);
        });
    
  }, []);

  const cancleOrder=()=>{
    window.location.reload(true)
  }

  return (

    <div> 
      {confirmModal&&
      <div className="fixed top-0 left-0 right-0 bottom-0 inset-x-0 px-3 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
      <div className="fixed inset-1 transition-opacity">
        <div className="absolute inset-1 bg-black opacity-75"></div>
      </div>
      <div className="bg-white text-lg rounded-lg px-14 p-10 items-center overflow-hidden shadow-xl transform transition-all sm:max-w-lg sm:w-full">
        <h1>Name: {user}</h1>
        <h1>Total Price: {total}</h1>
        <button
          className="relative left-40 bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-7 rounded focus:outline-none focus:shadow-outline"
          onClick={()=>{setOrderConfirmation(true)}}
        >
          confirm
        </button>
        <button
          className="relative left-40 bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-7 rounded focus:outline-none focus:shadow-outline"
          onClick={cancleOrder}

                  >
          cancle
        </button>
      </div>
    </div>}
    
    {orderConfirm&&
    <div className="fixed top-0 left-0 right-0 bottom-0 inset-x-0 px-3 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
      <div className="fixed inset-1 transition-opacity">
        <div className="absolute inset-1 bg-black opacity-75"></div>
      </div>
      <div className="bg-white text-lg rounded-lg px-14 p-10 items-center overflow-hidden shadow-xl transform transition-all sm:max-w-lg sm:w-full">
        <Result status="success" title="Order Successfull , Enjoy your meal!" />
        <button
          className="relative left-40 bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-7 rounded focus:outline-none focus:shadow-outline"
          onClick={onClick}
        >
          OK
        </button>
      </div>
    </div>}</div>
  );
};

export default OrderMsg;
