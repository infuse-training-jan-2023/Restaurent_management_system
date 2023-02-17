import React from "react";
import { useState, useEffect, useContext } from "react";
import logo from "../assets/logo.jpg";
import { Context } from "../context/CartContext";
import { InputNumber } from "antd";
import { AuthContext } from "../context/AuthContext";
import { FaTrashAlt } from "react-icons/fa";
import axios from "axios";

function CartItem({ item, onClick }) {
  const [quantity, setQuntity] = useState(item.quantity);
  const { user, signIn, signOut } = useContext(AuthContext);
  const updateCart = (value) => {
    const cartItem = {
      user_name: user,
      items: [
        {
          item_name: item.item_name,
          quantity: parseInt(value),
          price: item.price,
        },
      ],
    };

    axios
      .post("http://localhost:8000/cart", cartItem)
      .then((res) => {
        console.log(res.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <>
      <div class="flex bg-purple-100 border border-black rounded items-center hover:bg-gray-100 -mx-8 px-6 py-5 w-96">
        <div class="flex w-2/5">
          <div class="w-20">
            <span class="font-bold text-sm">{item.item_name}</span>
          </div>
          <div class="flex flex-col justify-left ml-4 flex-grow"></div>
        </div>
        <div class="flex justify-center w-1/5">
          <InputNumber
            autoFocus={true}
            min={1}
            defaultValue={quantity}
            onChange={(value) => {
              setQuntity(value);
              // TODO:
              updateCart(value);
            }}
          />
        </div>
        <span class="text-center w-1/5 font-semibold text-sm">
          {item.price}
        </span>
        <span class="text-center w-1/5 font-semibold text-sm">
          {item.price * quantity}
        </span>
        <button
          class="font-semibold hover:text-red-500 text-gray-500 text-xs ht-4"
          onClick={onClick}
        >
          {" "}
          <FaTrashAlt />
        </button>
      </div>
    </>
  );
}
export default CartItem;
