import React from "react";
import { Link } from "react-router-dom";
import logoImage from "../images/logo.png";
import "../App.css";

const Navbar = () => {
  return (
    <div id="navbar" className="navbar-container">
      <div className="logo">
        <img src={logoImage} alt="Logo" className="logo-image" />
        <span className="logo-text">RENT HOME KENYA</span>
      </div>
      <div className="menu">
        <Link to="/" className="nav-link">
          Home
        </Link>
        <Link to="/request-property" className="nav-link">
          Request a Property
        </Link>
        <Link to="/list-property" className="nav-link">
          List a Property
        </Link>
        <button className="contact-button">Contact us</button>
      </div>
    </div>
  )
}

export default Navbar