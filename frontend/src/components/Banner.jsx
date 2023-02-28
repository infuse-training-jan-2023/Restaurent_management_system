import React from "react";
import { useRef } from "react";

const Banner = ({ scrollToBottom }) => {
  return (
    <section className=" mt-32 w-full bg-yellow-50">
      <div className="flex flex-col mt-32 items-end pr-20 justify-center  header-banner bg-cover bg-no-repeat bg-left w-92 h-96 custom_banner_css">
        <div className="w-full text-center text-3xl md:text-4xl lg:text-5xl font-bold text-gray-700 pl-24 h1_div">
          <h1 className="w-3xl text-7xl text-left custom_h1">Best food </h1>
          <h1 className="w-3xl text-7xl text-left custom_h1"> waiting for you </h1> 
        </div>
        <div className="rounded-full p-1 box-border mt-8 overflow-hidden ring-red-300 focus:ring-4 w-full flex custom_reserve_table pl-24">
          <a href="#bottom" className="bg-primary px-24 py-3 overflow-hidden text-white poppins rounded-full ring-blue-300 focus:outline-none focus:ring-4 transform transition duration-700 hover:scale-105"
            style={{ zIndex: "1" }} onClick={scrollToBottom} >
            Reserve Table
          </a>
        </div>
      </div>
    </section>
  );
};

export default Banner;
