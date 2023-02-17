import React from "react";
import { useState, useEffect, useContext } from "react";
import { Context } from "../context/CartContext";
import { AuthContext } from "../context/AuthContext";
import axios from "axios";
import { message } from "antd";

const Menutab = () => {
  const info = () => {
    if (user) message.success("added to cart");
    else message.warning("user not logged");
  };
  const { user } = useContext(AuthContext);

  const fetchData = async () => {
    axios.get("http://localhost:8000/items").then((res) => {
      setFood(res.data.data);
      setFood(
        res.data.data.sort((a, b) => {
          if (a.price > b.price) return -1;
        })
      );
      console.log(res.data.data);
      console.log(res.data.data);
    });
  };
  const addToCart = ({ img, item_name, quantity, price, type }) => {
    if (user) {
      const cartItem = {
        user_name: user,
        items: [
          {
            item_name: item_name,
            quantity: 1,
            price: price,
          },
        ],
      };

      axios
        .post("http://localhost:8000/cart", cartItem)
        .then((res) => {
          console.log(res.data.data);
        })
        .catch((error) => {
          console.error(error);
        });

      setContext(item_name);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const changeMenuTabs = (type) => {
    setMenuTab(type);
  };

  const [sortType, setSortType] = useState("albums");

  useEffect(() => {
    const sortedList =
      sortType == "low"
        ? [...foods].sort((a, b) => {
            if (a.price < b.price) return -1;
          })
        : [...foods].sort((a, b) => {
            if (a.price > b.price) return -1;
          });
    setFood(sortedList);
  }, [sortType]);

  const [menuTab, setMenuTab] = useState("all");
  const [foods, setFood] = useState([]);
  const [context, setContext] = useContext(Context);
  const [query, setQuery] = useState("");

  const filteredData = [...foods].filter((item) => {
    return item.item_name.toLowerCase().includes(query.toLowerCase());
  });
  return (
    <section className="bg-orange-50 my-12 mt-1 py-10 max-w-screen-xl mx-auto px-6">
      <div className="flex items-center justify-center space-x-6">
        <div className="rounded-full p-1 box-border bg-white border border-black overflow-hidden ring-red-300 focus:ring-4 w-82 flex items-center custom_search_css">
          <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-red-300 focus:ring-4 transition duration-300 hover:scale-105 ">
            Search
          </button>
          <input
            type="text"
            className=" rounded-full px-4 focus:outline-none w-full border-solid border-black bg-transparent"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="search your food....."
          />
        </div>

        <div className="flex">
          <button
            className="food-filters custom_btn_css food_icon1"
            onClick={() => changeMenuTabs("all")}
          >
            <img className=" h-12" src="../../public/breakfast.png" />
            All
          </button>
          <button
            className="food-filters custom_btn_css food_icon2"
            onClick={() => changeMenuTabs("snacks")}
          >
            <img className=" h-12" src="../../public/burger.png" />
            Snacks
          </button>
          <button
            className="food-filters custom_btn_css food_icon3"
            onClick={() => changeMenuTabs("meals")}
          >
            <img className=" h-12" src="../../public/dinner.png" />
            Meals
          </button>
          <button
            className="food-filters custom_btn_css food_icon4"
            onClick={() => changeMenuTabs("beverages")}
          >
            <img className="h-12" src="../../public/beverage.png" />
            Beverages
          </button>
        </div>

        <span className="rounded-full box-border bg-white border border-black overflow-hidden flex items-center p-1 custom_sort_css">
          <label className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-red-300 focus:ring-4 transition duration-300 hover:scale-105">
            Sort
          </label>
          <select
            class="text-center w-28 p-1 py-2 rounded-full focus:outline-none border-solid border-black bg-transparent"
            onChange={(e) => setSortType(e.target.value)}
          >
            <option value="high">high-low</option>
            <option value="low">low-high</option>
          </select>
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 mt-5 overflow-y-scroll h-96 ">
        {query.length > 0
          ? filteredData.map((item) => (
              <FoodCard
                {...item}
                onClick={() => {
                  info();
                  addToCart(item);
                }}
              />
            ))
          : menuTab === "all"
          ? foods.map((item) => (
              <FoodCard
                {...item}
                onClick={() => {
                  info();
                  addToCart(item);
                }}
              />
            ))
          : foods
              .filter((item) => menuTab === item.tag)
              .map((item) => (
                <FoodCard
                  {...item}
                  onClick={() => {
                    info();
                    addToCart(item);
                  }}
                />
              ))}
      </div>
    </section>
  );
};

const FoodCard = ({ img, item_name, description, price, onClick }) => {
  return (
    <div className="inline-block px-2 w-84 rounded-full custom_card_css">
      <div className="w-96 h-84 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-2xl transition-shadow  duration-300 ease-in-out ">
        <div className="bg-white border border-gray-100 transition  duration-700 hover:shadow-xl p-4 rounded-lg">
          <img
            className=" w-84 h-44 mx-auto transition duration-300 hover:scale-110"
            src={`data:image/jpeg;base64,${img}`}
            alt=""
          />
          <div className="h-36 flex flex-col items-center my-3 space-y-2">
            <h1 className="text-gray-900 poppins text-lg">{item_name}</h1>
            <h2 className="text-gray-900 poppins text-2xl font-bold">
              &#8377;{price}
            </h2>
            <button
              className="bg-primary text-white px-8 py-2 focus:outline-none poppins rounded-full mt-24 transition duration-300 hover:scale-105"
              onClick={onClick}
            >
              Add to cart
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Menutab;
