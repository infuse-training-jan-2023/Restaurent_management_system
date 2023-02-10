import React from "react";
import { useState,useEffect } from "react";
import logo from '../assets/logo.jpg';
import axios from 'axios'
const Menutab =()=>
{   
    const fetchData = async () => {
        axios.get('http://localhost:8000/items')
          .then(res => {
            setFood(res.data)
            console.log(res.data);
          })
      };  

      useEffect(() => {
        fetchData()
      },[]);

    const changeMenuTabs = (type) => {
        setMenuTab(type)
    }
    const [menuTab, setMenuTab] = useState('snacks')
    const [foods ,setFood] = useState([])
    
    return(
    <section className="my-12 max-w-screen-xl mx-auto px-6">
            <div className="flex items-center justify-center space-x-6">
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 " onClick={() => changeMenuTabs('snacks')}>Breakfast</button>            
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 "onClick={() => changeMenuTabs('Lunch')}>Lunch</button>           
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 " onClick={() => changeMenuTabs('Dinner')}>Dinner</button>            
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-12">
                {foods.filter((item) => menuTab === item.tag).map(item =>( <FoodCard key={item._id} {...item} />
                ))}
            </div>            
    </section>)
}

const FoodCard = ({ img, item_name, description, price, type}) => {
   
    return (
        <div className="bg-white border border-gray-100 transition transform duration-700 hover:shadow-xl hover:scale-105 p-4 rounded-lg relative">
            <img className="w-64 mx-auto transform transition duration-300 hover:scale-105" src={`data:image/jpeg;base64,${img}`} alt="" />
            <div className="flex flex-col items-center my-3 space-y-2">
                <h1 className="text-gray-900 poppins text-lg">{item_name}</h1>
                <h2 className="text-gray-900 poppins text-2xl font-bold">&#8377;{price}</h2>
                <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transform transition duration-300 hover:scale-105" onClick>Order Now</button>
            </div>
        </div>
    )
  } 

export default Menutab