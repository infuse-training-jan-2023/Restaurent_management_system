import React from "react";
import { FaShoppingCart } from "react-icons/fa";
import logo from "../assets/logo.jpg";
import { Avatar, Badge } from "antd";
import { useState, useContext, useEffect } from "react";
import { Context } from "../context/CartContext";
import axios from "axios";
import CartItem from "./cart";
import OrderMsg from "./OrderSuccess";
import { AuthContext } from "../context/AuthContext";
import { Drawer } from "antd";
import { UserOutlined } from "@ant-design/icons";

const CartContext = React.createContext();

const Header = () => {
  const [showCart, setShowCart] = useState("");
  const [isShown, setIsShown] = useState("");
  const [cartItems, setCartItems] = useState([]);
  const [cartsize, setCartSize] = useState(0);
  const [context, setContext] = useContext(Context);
  const { user, signIn, signOut } = useContext(AuthContext);
  const [open, setOpen] = useState(false);
  const [ordermsg, setOrdermsg] = useState(false);
  const [total, settotal] = useState("");
  const [showorder, setShoworder] = useState(false);

  const showDrawer = () => {
    setOpen(true);
  };

  const createOrder = () => {
    axios
      .delete(`http://localhost:8000/checkout/${user}`)
      .then((res) => {
        console(res.data.items);
      })
      .catch((error) => {
        console.error(error);
      });
    setCartItems([]);
    setCartSize(0);
    setShoworder(false);
  };
  const deleteCartItem = (deleteItem) => {
    const modifiedData = cartItems.filter((item) => item !== deleteItem);
    setCartItems(modifiedData);
    setCartSize(modifiedData.length)
    axios
      .delete(`http://localhost:8000/cart/${user}/${deleteItem.item_name}`)
      .then((res) => {
        console(res.data.items);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const showOrderStatus = () => {
    setShoworder(true);
    setCartSize(0);
    setOrdermsg(true);
    closeCart();
    setCartItems([]);
  };
  const closeCart = () => {
    setOpen(false);
    setShowCart((current) => !current);
  };
  const show_login_modal = () => {
    setIsShown((current) => !current);
  };

  const show_cart_modal = () => {
    if (user) {
      showDrawer();
      setShowCart((current) => !current);
    } else setIsShown((current) => !current);
  };

  const log_out = () => {
    signOut();
    setCartSize(0);
    window.location.reload(true);
  };
  const log_in = (event) => {
    event.preventDefault();
    signIn(event.target.username.value);
    show_login_modal();
  };
  useEffect(() => {
    if (user) {
      axios
        .get(`http://localhost:8000/cart/${user}`)
        .then((res) => {
          setCartItems(res.data.items);
          settotal(res.data.grand_total);
          console.log(res.data);
          setCartSize(res.data.items.length);
        })
        .catch((error) => {
          console.error(error);
        });
    }
  }, [user, context, showCart]);

  return (
    <>
      <CartContext.Provider value={{ cartItems }}>
        <Context.Provider value={context}>
          <nav className="flex fixed w-full top-0 items-center justify-between border-4 border-white rounded-lg flex-wrap bg-orange-50 p-6">
            <div className="flex items-center flex-shrink-0 text-white mr-6">
              <img src={logo} className="h-12 rounded-full my-4" />
              <span className="font-semibold text-xl tracking-tight"></span>
            </div>
            <div className="block lg:hidden">
              <button className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white">
                <svg
                  className="fill-current h-3 w-3"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <title>Menu</title>
                  <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
                </svg>
              </button>
            </div>
            <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
              <div className="text-sm lg:flex-grow">
                <a
                  href="#responsive-header"
                  className="bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-3 mr-2 "
                >
                  Reserve Table
                </a>
                {!user && (
                  <button
                    className="bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-3 mr-2 "
                    onClick={show_login_modal}
                  >
                    SignIn
                  </button>
                )}
              </div>

              {user && (
                <span>
                  <div className="text-3xl font-medium text-white-900 dark:text-white  px-4 block poppins rounded-full mt-4 lg:inline-block lg:mt-0 text-black">
                    Hi {user}{" "}
                    <span>
                      <Avatar
                        size="large"
                        style={{ backgroundColor: "gray" }}
                        icon={<UserOutlined />}
                      />
                    </span>
                  </div>
                  <button
                    className="bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-3 mr-2 "
                    onClick={log_out}
                  >
                    Logout
                  </button>
                </span>
              )}

              <div>
                <Badge count={user ? cartsize : 0}>
                  <button
                    className=" bg-primary px-6 py-3 text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105 py-4"
                    onClick={show_cart_modal}
                  >
                    <FaShoppingCart />
                  </button>
                </Badge>
              </div>
            </div>

            {isShown && (
              <div className="fixed top-0 left-0 right-0 bottom-0 inset-x-0 px-3 pb-4 sm:inset-0 sm:flex sm:items-center sm:justify-center">
                <div className="fixed inset-1 transition-opacity">
                  <div className="absolute inset-1 bg-black opacity-75"></div>
                </div>
                <div className="bg-white text-lg rounded-lg px-14 p-10  overflow-hidden shadow-xl transform transition-all sm:max-w-lg sm:w-full">
                  <form className="text-center" onSubmit={log_in}>
                    <h2 className="text-lg font-medium mb-">Login</h2>
                    <div className="mb-5">
                      <label className="block mb-2 text-sm font-medium text-black-0">
                        Username
                      </label>
                      <input
                        className="w-full px-3 py-2 text-sm leading-tight bg-black-200 border border-black rounded appearance-none focus:outline-none focus:bg-white"
                        id="username"
                        name="username"
                        required
                        type=""
                        placeholder="user"
                      />
                    </div>
                    <div className="mb-6">
                      <label className="block mb-2 text-sm font-medium text-black">
                        Password
                      </label>
                      <input
                        className="w-full px-3 py-2 text-sm leading-tight text-black-700 bg-black-200 border border-black rounded appearance-none focus:outline-none focus:bg-white"
                        id="password"
                        type="password"
                        required
                        placeholder="Password"
                      />
                    </div>
                    <div className="flex items-center justify-between">
                      <button
                        className="bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        type="submit"
                      >
                        Sign In
                      </button>
                      <button
                        onClick={show_login_modal}
                        className="text-sm font-medium text-teal-500 hover:text-teal-400"
                      >
                        Cancel
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            )}

            {showCart && (
              <>
                <Drawer
                  width={600}
                  placement="right"
                  onClose={closeCart}
                  open={open}
                >
                  <div class="w-3/4 bg-white px-10 py-10">
                    <div class="flex justify-between border-b pb-8">
                      <h1 class="font-semibold text-2xl">Cart</h1>
                    </div>
                    <div class="flex mt-10 mb-5">
                      <h3 class="font-semibold text-gray-600 text-xs uppercase w-2/5">
                        Product Details
                      </h3>
                      <h3 class="font-semibold text-center text-gray-600 text-xs uppercase w-1/5 text-center">
                        Quantity
                      </h3>
                      <h3 class="font-semibold text-center text-gray-600 text-xs uppercase w-1/5 text-center">
                        Price
                      </h3>
                      <h3 class="font-semibold text-center text-gray-600 text-xs uppercase w-1/5 text-center">
                        Total
                      </h3>
                    </div>
                    {cartItems.map((item, index) => (
                      <CartItem
                        key={index}
                        item={item}
                        onClick={() => deleteCartItem(item)}
                      />
                    ))}
                  </div>
                  <div>
                    {cartsize > 0 ? (
                      <button
                        className="bg-teal-500 hover:bg-teal-400 text-white font-medium py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        onClick={showOrderStatus}
                      >
                        Checkout
                      </button>
                    ) : (
                      <div className="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700">
                        No item in cart
                      </div>
                    )}
                  </div>
                </Drawer>
              </>
            )}
            {showorder && <OrderMsg onClick={() => createOrder()} />}
          </nav>
        </Context.Provider>
      </CartContext.Provider>
    </>
  );
};

export default Header;
