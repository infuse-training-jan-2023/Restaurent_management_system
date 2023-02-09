import React from "react";
import { useState } from "react";
import logo from '../assets/logo.jpg';

const Menutab =()=>
{   
    const changeMenuTabs = (type) => {
        setMenuTab(type)
    }
    const [menuTab, setMenuTab] = useState('Breakfast')
    const [foods ,setFood] = useState([{'image':'kdfj', 'title':'breakfast', 'description':'100', 'price':"100", 'foodType':'Breakfast'},{'image':'kdfj', 'title':'lunch', 'description':'100', 'price':"100", 'foodType':'Lunch'},{'image':'kdfj', 'title':'Dinner', 'description':'100', 'price':"100", 'foodType':'Dinner'}])

    return(
    <section className="my-12 max-w-screen-xl mx-auto px-6">
            <div className="flex items-center justify-center space-x-6">
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 transform" onClick={() => changeMenuTabs('Breakfast')}>Breakfast</button>            
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 transform"onClick={() => changeMenuTabs('Lunch')}>Lunch</button>           
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 transform" onClick={() => changeMenuTabs('Dinner')}>Dinner</button>            
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-12">
                {foods.filter((item) => menuTab === item.foodType).map(item => ( <FoodCard key={item._id} {...item} />
                ))}
            </div>            
    </section>)
}

const FoodCard = ({ image, title, description, price, foodType}) => {

    return (
        <div className="bg-white border border-gray-100 transition transform duration-700 hover:shadow-xl hover:scale-105 p-4 rounded-lg relative">
            <img className="w-64 mx-auto transform transition duration-300 hover:scale-105" src={logo} alt="" />
            <div className="flex flex-col items-center my-3 space-y-2">
                <h1 className="text-gray-900 poppins text-lg">{title}</h1>
                <h2 className="text-gray-900 poppins text-2xl font-bold">&#8377;{price}</h2>
                <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transform transition duration-300 hover:scale-105" onClick>Order Now</button>
            </div>
        </div>
    )
  } 

export default Menutab