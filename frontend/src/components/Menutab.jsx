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
            setFood(res.data.data)
            setFood(res.data.data.sort((a,b)=>{
              if (a.price >b.price) return -1;
            }))
            console.log(res.data.data);
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
    const sortItems = () => {
      console.log("methodcalled");
      setFood(foods.sort((a,b)=>{
        if (a.price < b.price) return -1;
      }))
      console.log(foods)
    }
    const [sortType, setSortType] = useState('albums');

    useEffect(() => {
      const sortedList = ( sortType=='low' ? [...foods].sort((a,b)=>{
        if (a.price < b.price) return -1;
      }):[...foods].sort((a,b)=>{
        if (a.price > b.price) return -1;
      }))

      setFood(sortedList)
    },[sortType])

    const [menuTab, setMenuTab] = useState('all')
    const [foods ,setFood] = useState([])
    const [context, setContext] = useContext(Context);
    return(
    <section className="bg-orange-50 my-12 py-10 max-w-screen-xl mx-auto px-6">
            
            <div className="flex items-center justify-center space-x-6">
                <button className="btn" onClick={() => changeMenuTabs('all')}>All</button>            
                <button className="btn" onClick={() => changeMenuTabs('snacks')}>Snacks</button>            
                <button className="btn "onClick={() => changeMenuTabs('meals')}>Meals</button>           
                <button className="btn " onClick={() => changeMenuTabs('beverages')}>Beverages</button>   
                <span>
                <label className="p-2">Sort</label>
                <select onChange={(e) => setSortType(e.target.value)}>
                <option value="high">high-low</option>
                <option value="low">low-high</option>
                </select>
                <label className="p-2">FoodType</label>
                <select onChange={(e) => setFoodType(e.target.value)}>
                <option></option>
                <option value="veg">Veg</option>
                <option value="non-veg">Non-veg</option>
                </select>
                </span>         
            </div>  
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-20 overflow-y-scroll h-96">
            {menuTab==='all'? foods.map(item=>(<FoodCard key={item._id} {...item} onClick={()=>{addToCart(item)}} />)):
          foods.filter((item) => menuTab === item.tag).map(item =>(<FoodCard {...item} onClick={()=>{addToCart(item)}} />
           ))}
          </div>
{/* {<div class="flex flex-col bg-white m-auto p-auto">
      <div className=" flex overflow-x-scroll pb-10 -h-1 hide-scroll-bar">
        <div className="flex flex-nowrap lg:ml-40 md:ml-20 ml-10 ">
          <div class="inline-block px-4 ">
            <div className=" w-auto h-96 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out">
            </div>
          </div>
          {menuTab==='all'? foods.map(item=>(<FoodCard key={item._id} {...item} onClick={()=>{addToCart(item)}} />)):
          foods.filter((item) => menuTab === item.tag).map(item =>(<FoodCard key={item._id} {...item} onClick={()=>{addToCart(item)}} />
           ))}
          
        </div>
      </div>
</div>} */}
       
    </section>
    )
}

const FoodCard = ({ img, item_name, description, price,onClick}) => {
  return (
    <div className="inline-block px-2 w-84 h-">
    <div className="w-96 h-84 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-2xl transition-shadow  duration-300 ease-in-out "><div className="bg-white border border-gray-100 transition  duration-700 hover:shadow-xl p-4 rounded-lg">
      <img className=" w-84 h-44 mx-auto transition duration-300 hover:scale-110" src={`data:image/jpeg;base64,${img}`} alt="" />
    <div className="h-36 flex flex-col items-center my-3 space-y-2">
        <h1 className="text-gray-900 poppins text-lg">{item_name}</h1>
        <h2 className="text-gray-900 poppins text-2xl font-bold">&#8377;{price}</h2>
        <button className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transition duration-300 hover:scale-105" onClick={onClick}>Add to cart</button>
    </div></div>
    </div>
  </div>
    )
} 

export default Menutab