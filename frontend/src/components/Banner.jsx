import React from 'react'
const Banner = () => {
    return (
      
        <section className=" header-banner mt-32 w-full bg-yellow-50">
            <div className="flex flex-col mt-32 items-center justify-center h-full">
                <h1 className="pl-24 text-center text-3xl md:text-4xl lg:text-5xl poppins font-bold text-gray-700 ">Best food waiting for you</h1>
                <div className="rounded-full p-1 box-border mt-8 bg-white overflow-hidden ring-red-300 focus:ring-4 w-96 flex items-center">
                    <input type="text" className=" rounded-full px-4 focus:outline-none w-full bg-transparent" placeholder="Search ....." />
                    <button className="text-sm bg-primary py-3 px-6 rounded-full text-white poppins ring-red-300 focus:ring-4 transition duration-300 hover:scale-105 ">Search</button>
                </div>
            </div>
        </section>
    )
}

export default Banner