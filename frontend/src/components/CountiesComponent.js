import React from "react";
import "../App.css";
import Navbar from "../layout/Navbar";
import Footer from "../layout/Footer";

export default function CountiesComponent() {
    return (
        <div className="Search">
            <Navbar/>
            <h3>The counties</h3>
            <Footer/>
        </div>
    );
}