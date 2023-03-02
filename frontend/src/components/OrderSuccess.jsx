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
        .get(`https://kmynmmc7kh.execute-api.ap-south-1.amazonaws.com/fastapi/api/cart/${user}`)
        .then((res) => {
          settotal(res.data.data.grand_total);
        })
        .catch((error) => {
          console.error(error);
        });
    
  }, []);

  const cancelOrder=()=>{
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
        <h1 className="text-center" >Name: <span className="uppercase font-semibold">{user}</span></h1>
        <h1 className="text-center">Total Price:<span className="pl-2 font-semibold">&#8377; {total}</span> </h1>
        <div className="py-4">
        <button 
          className="relative bg-teal-500 left-14 hover:bg-teal-400 text-white font-medium py-2 px-7 rounded focus:outline-none focus:shadow-outline"
          onClick={()=>{setOrderConfirmation(true)}}>
          confirm
        </button>
        <button
          className="relative ml-10 left-20 bg-red-500 hover:bg-red-400 text-white font-medium py-2 px-7 rounded focus:outline-none focus:shadow-outline"
          onClick={cancelOrder}>
          cancel
        </button>
        </div>
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
