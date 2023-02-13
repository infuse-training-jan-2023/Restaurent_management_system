import React from "react";
import { useState,useEffect ,useContext} from "react";
import {Context} from '../context/CartContext'
import { AuthContext } from '../context/AuthContext';

import axios from 'axios'
const Menutab =()=>
{   
  const { user } = useContext(AuthContext);

    const fetchData = async () => {
        axios.get('http://localhost:8000/items')
          .then(res => {
            setFood(res.data)
            console.log(res.data);
          })
      }; 
      console.log(user)
      const addToCart=({ img, item_name, quantity, price, type}) => {
       if(user){ 
        const cartItem = {
          
            "user_name":user,
            "items": [
              {
                "item_name": item_name,
                "quantity": 1,
                "price": price
              }
            ]
          
          };
      
          axios.post('http://localhost:8000/cart', cartItem)
            .then(res => {
              console.log(res.data);
            })
            .catch(error => {
              console.error(error);
            });

        setContext(item_name)}
      } 

      useEffect(() => {
        fetchData()
      },[]);

    const changeMenuTabs = (type) => {
        setMenuTab(type)
    }
    const [menuTab, setMenuTab] = useState('snacks')
    const [foods ,setFood] = useState([])
    const [context, setContext] = useContext(Context);
    return(
    <section className="my-12 max-w-screen-xl mx-auto px-6">
            
            <div className="flex items-center justify-center space-x-6">
                <button className="btn" onClick={() => changeMenuTabs('snacks')}>Breakfast</button>            
                <button className="btn "onClick={() => changeMenuTabs('Lunch')}>Lunch</button>           
                <button className="btn " onClick={() => changeMenuTabs('Dinner')}>Dinner</button>            
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-12">
                {foods.filter((item) => menuTab === item.tag).map(item =>( <FoodCard key={item._id} {...item} onClick={()=>{addToCart(item)}} />
                ))}
            </div>            
    </section>
    )
}

const FoodCard = ({ img, item_name, description, price,onClick}) => {
  return (
        <div className="bg-white border border-gray-100 transition  duration-700 hover:shadow-xl p-4 rounded-lg">
            <img className="w-64 mx-auto transition duration-300 " src={`data:image/jpeg;base64,${img}`} alt="" />
            <div className="flex flex-col items-center my-3 space-y-2">
                <h1 className="text-gray-900 poppins text-lg">{item_name}</h1>
                <h2 className="text-gray-900 poppins text-2xl font-bold">&#8377;{price}</h2>
                <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transition duration-300 hover:scale-105" onClick={onClick}>Add to cart</button>
            </div>
        </div>
    )
} 

export default Menutab