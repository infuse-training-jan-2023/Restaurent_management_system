import React from "react";
import { FaShoppingCart } from 'react-icons/fa';
import logo from '../assets/logo.jpg';
import { Avatar, Badge} from 'antd';
import {useState} from 'react'

const Header = () => {
  const [isShown, setIsShown] = useState(false);

  const show_login_modal = () => {

    setIsShown(current => !current);
  };
  return (
    <nav className="flex fixed w-full top-0 items-center justify-between flex-wrap bg-teal-500 p-6">
      <div className="flex items-center flex-shrink-0 text-white mr-6">
      <img src={logo}className='h-12 rounded-full'/>
        <span className="font-semibold text-xl tracking-tight"></span>
      </div>
      <div className="block lg:hidden">
        <button className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white">
          <svg className="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
        </button>
      </div>
      <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
        <div className="text-sm lg:flex-grow">
          <a href="#responsive-header" className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
            Reserve Table
          </a>
          <button className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white " onClick={show_login_modal}>
            signin
          </button>
          
        </div>
        <div>
        <Badge count={1}>
      <button className=" bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-4"><FaShoppingCart/></button></Badge>
        </div>
      </div>
      {isShown &&       
      <div className="relative">
        <div className="fixed top-0 left-0 right-0 bottom-0 opacity-100 bg-black z-50">
          <div className="flex items-center justify-center h-full mx-auto">
            <div className="bg-white p-16 rounded-lg shadow-xl">
              <form className="text-center">
                <h2 className="text-lg font-medium mb-6">Login</h2>
                <div className="mb-5">
                  <label className="block mb-2 text-sm font-medium text-black-0">
                    Username
                  </label>
                  <input className="w-full px-3 py-2 text-sm leading-tight bg-black-200 border border-black rounded appearance-none focus:outline-none focus:bg-white" id="email" type="" placeholder="Email" />
                </div>
                <div className="mb-6">
                  <label className="block mb-2 text-sm font-medium text-black">
                    Password
                  </label>
                  <input className="w-full px-3 py-2 text-sm leading-tight text-black-700 bg-black-200 border border-black rounded appearance-none focus:outline-none focus:bg-white" id="password" type="password" placeholder="Password" />
                </div>
                <div className="flex items-center justify-between">
                  <button className="bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                    Sign In
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
    </nav>
    
  );
};



export default Header;
