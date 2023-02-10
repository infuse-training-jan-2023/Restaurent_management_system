import React from "react";
import { FaShoppingCart } from 'react-icons/fa';
import logo from '../assets/logo.jpg';
const Navbar = () => {
  return (
    
            <> 
            <div className="flex justify-start space-x-9 mb-4 my-2 mx-auto w-full">
            <img src={logo}className='h-12 rounded-full'/>
            <button className=" bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105">LogIn</button>
            <button className=" bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 ">Reserve Table</button>
            <button className=" bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-4"><FaShoppingCart/></button>
            </div>
            </>
  )
}

export default Navbar