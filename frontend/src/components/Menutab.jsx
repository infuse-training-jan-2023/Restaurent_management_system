import React from "react";
import { useState,useEffect } from "react";
import logo from '../assets/logo.jpg';
import axios from 'axios'
import { List } from "antd";
import Mycontext from '../context/cartcont'
const Menutab =()=>
{
    const [cartlist ,setcartlist]= useState('');

    const addtocart = ({ img, item_name, description, price, type}) => {

        console.log("item name: "+item_name, "item price: "+ price)
        // if (item_name in cartlist)
        // {
        //     console.log(item_name +" is present");
        //     console.log(cartlist)
        // }
        // else
        // {
        //     setcartlist({...cartlist, [item_name]:price})
        //     console.log(cartlist)
        // }

        localStorage.setItem(item_name, price);
        setcartlist(localStorage.length)

    }


    // setcartlist(prev=>{
            //     console.log({...prev, [item_name]:price})
            //     return {...prev, [item_name]:price}
            // });
            // console.log(cartlist)

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
        <>
   <Mycontext.Provider value={{counter:cartlist}}>
    <section className="my-12 max-w-screen-xl mx-auto px-6">
            <div className="flex items-center justify-center space-x-6">
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 " onClick={() => changeMenuTabs('snacks')}>Breakfast</button>
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 "onClick={() => changeMenuTabs('Lunch')}>Lunch</button>
                <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-blue-300 focus:ring-4 transition duration-300 hover:scale-105 " onClick={() => changeMenuTabs('Dinner')}>Dinner</button>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-12">
                {foods.filter((item) => menuTab === item.tag).map(item =>( <FoodCard key={item._id} {...item} onClick={()=>{addtocart(item)}}/>
                ))}
            </div>
    </section>
    </Mycontext.Provider>
    </>   )
}

const FoodCard = ({ img, item_name, description, price, type, onClick}) => {

    return (
        <div className="bg-white border border-gray-100 transition  duration-700 hover:shadow-xl hover:scale-105 p-4 rounded-lg relative">
            <img className="w-64 mx-auto transition duration-300 hover:scale-105" src={`data:image/jpeg;base64,${img}`} alt="" />
            <div className="flex flex-col items-center my-3 space-y-2">
                <h1 className="text-gray-900 poppins text-lg">{item_name}</h1>
                <h2 className="text-gray-900 poppins text-2xl font-bold">&#8377;{price}</h2>
                <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transition duration-300 hover:scale-105" onClick={onClick}>Order Now</button>
            </div>
        </div>
    )
}

export default Menutab
