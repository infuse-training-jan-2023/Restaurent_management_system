import React from "react";
import logo from '../assets/dining-table.png';

const Table = ()=>
{
    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-12">
          <div className="background-color: rgb(252 165 165);
 border border-gray-100 transition transform duration-700 hover:shadow-xl hover:scale-105 p-4 rounded-lg relative">
           
           <div></div>
            
        </div>
        <div className=" border border-gray-100 transition transform duration-700 hover:shadow-xl hover:scale-105 p-4 rounded-lg relative">
            <img className="w-10 mx-20 transform transition duration-300 hover:scale-105" src={logo} alt="" />
            <div className="flex flex-col items-center my-3 space-y-2">
                
                <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transform transition duration-300 hover:scale-105" onClick>Order Now</button>
            </div>
            
        </div> <div className="bg-white border border-gray-100 transition transform duration-700 hover:shadow-xl hover:scale-105 p-4 rounded-lg relative">
            <img className="w-64 mx-auto transform transition duration-300 hover:scale-105" src={logo} alt="" />
            <div className="flex flex-col items-center my-3 space-y-2">
                
                <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transform transition duration-300 hover:scale-105" onClick>Order Now</button>
            </div>
            
        </div> <div className="bg-white border border-gray-100 transition transform duration-700 hover:shadow-xl hover:scale-105 p-4 rounded-lg relative">
            <img className="w-64 mx-auto transform transition duration-300 hover:scale-105" src={logo} alt="" />
            <div className="flex flex-col items-center my-3 space-y-2">
                
                <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transform transition duration-300 hover:scale-105" onClick>Order Now</button>
            </div>
            
        </div>
        </div>
        )
}
export default Table