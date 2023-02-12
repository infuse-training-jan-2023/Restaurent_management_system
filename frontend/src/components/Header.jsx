import React from "react";
import { FaShoppingCart } from 'react-icons/fa';
import logo from '../assets/logo.jpg';
import { Avatar, Badge} from 'antd';
import {useState,useContext,useEffect} from 'react'
import AuthContext from '../context/usercontext'
import {Context} from '../context/usercontext copy'
import {Username} from '../context/username'
import axios from 'axios'
const CartContext = React.createContext();

const Header = () => {
  const [showCart, setShowCart] = useState('');

  const [isShown, setIsShown] = useState('');
  const [authname, setauthname] = useState('');
  const [authstatus, setauthstatus] = useState(true);
  const [username, setUsername] = useContext(Username);
  const [cartItems, setCartItems] = useState([]);
  const [cartsize, setCartSize] = useState(0)
  const [context, setContext] = useContext(Context);

  const show_login_modal = () => {
    setIsShown(current => !current);
  };

  const show_cart_modal = () => {
    if (!authstatus)
    setShowCart(current => !current);
  };

  const log_out= () => {
    setauthname('');
    setauthstatus(true)
    setCartSize(0);
  }
  const log_in = event => {
    event.preventDefault();
    setauthname(event.target.username.value);
    setUsername(event.target.username.value);
    setauthstatus(false)
    show_login_modal()
  };
  useEffect(() => {
    if (!authstatus) {
      axios.get(`http://localhost:8000/cart/${username}`)
        .then(res => {
          setCartItems(res.data.items);
          setCartSize(res.data.items.length);
        })
        .catch(error => {
          console.error(error);
        })
    }
  },[authstatus,context]);


    return (
    <>
    <AuthContext.Provider value={{ username:authname,status:authstatus}}>
    <CartContext.Provider value={{ cartItems }}>
    <Context.Provider value={context}>
    <nav className="flex fixed w-full top-0 items-center justify-between flex-wrap bg-teal-500 p-6">
      <div className="flex items-center flex-shrink-0 text-white mr-6">
      <img src={logo}className='h-12 rounded-full my-4'/>
        <span className="font-semibold text-xl tracking-tight"></span>
      </div>
      <div className="block lg:hidden">
        <button className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white">
          <svg className="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
        </button>
      </div>
      <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
        <div className="text-sm lg:flex-grow">
          <a href="#responsive-header" className="bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-3 mr-2 ">
            Reserve Table
          </a>
          { authstatus && (<button className="bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-3 mr-2 " onClick={show_login_modal}>
            SignIn
          </button>)}


        </div>
        <div>
        {/* {<div className="py-3 px-4 block poppins rounded-full mt-4 lg:inline-block lg:mt-0 text-white">
          Hi {username}
        </div> } */}
        { !authstatus && (<span>
          <div className="py-3 px-4 block poppins rounded-full mt-4 lg:inline-block lg:mt-0 text-white">
          Hi {username}
        </div>
        <button className="bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-3 mr-2 " onClick={log_out}>
            Logout
          </button></span>)}

        <Badge count={authstatus? 0:cartsize}>

      <button className=" bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-4" onClick={show_cart_modal}><FaShoppingCart/></button></Badge>
        </div>
      </div>

      {isShown &&
      <div className="w-2">
        <div className="fixed  top-0 left-0 right-0 bottom-0 opacity-80 bg-black z-50">
          <div className="flex items-center justify-center h-full ">
            <div className="bg-white p-16  rounded-lg shadow-xl">
              <form className="text-center" onSubmit={log_in}>
                <h2 className="text-lg font-medium mb-6">Login</h2>
                <div className="mb-5">
                  <label className="block mb-2 text-sm font-medium text-black-0">
                    Username
                  </label>
                  <input className="w-full px-3 py-2 text-sm leading-tight bg-black-200 border border-black rounded appearance-none focus:outline-none focus:bg-white" id="username" name="username" required type="" placeholder="user" />
                </div>
                <div className="mb-6">
                  <label className="block mb-2 text-sm font-medium text-black">
                    Password
                  </label>
                  <input className="w-full px-3 py-2 text-sm leading-tight text-black-700 bg-black-200 border border-black rounded appearance-none focus:outline-none focus:bg-white" id="password" type="password" required placeholder="Password" />
                </div>
                <div className="flex items-center justify-between">
                  <button className="bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
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

{showCart &&




<div className="w-2">
        <div className="fixed  top-0 left-0 right-0 bottom-0 bg-black z-50">
          <div className="flex items-center justify-center h-full ">
            <div className="bg-white p-16  rounded-lg shadow-xl">
            {
         cartItems.map((item, index) => (
           <CartItem key={index} item={item} />
         ))}

                  <button onClick={show_cart_modal} className="text-sm font-medium text-teal-500 hover:text-teal-400">
                    Cancel
                  </button>
                </div>
            </div>
          </div>
        </div>



      }
    </nav>
    </Context.Provider>
    </CartContext.Provider>

    </AuthContext.Provider>

    </>
  );
};


function CartItem({ item }) {
  return (



		<li className="flex items-start justify-between">
			<h3>{item.item_name}
				<span className="text-sm dark:text-violet-400">x{item.quantity}</span>
			</h3>
			<div className="text-right">
				<span className="block">{item.price}</span>
			</div>
		</li>


  );
}
export default Header;
