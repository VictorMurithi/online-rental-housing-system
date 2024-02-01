// Apartments.js
import React, { useState, useEffect } from "react";
import { useParams ,} from "react-router-dom";
import Navbar from "../layout/Navbar";
import Footer from "../layout/Footer";

const Apartments = () => {
  const [apartments, setApartments] = useState([]);
  const { county } = useParams();

  useEffect(() => {
    // Ensure that 'county' is defined before making the fetch request
    if (county) {
      fetch(`/counties/${county}/apartments`)
        .then(response => response.json())
        .then(data => {
          // Check if the array is not empty and extract the first element
          const firstApartment = data.length > 0 ? data[0] : null;
  
          if (firstApartment) {
            console.log("apartment:", firstApartment);
            setApartments([firstApartment]);
          } else {
            console.log("No apartments found for the specified county.");
            setApartments([]);
          }
        })
        .catch(error => {
          console.error("Error fetching apartments:", error);
        });
    }
  }, [county]);
  

  return (
    <div>
      <Navbar />
      <h1>Apartments in {county}</h1>
      <div className="apartments-container">
        {apartments.length === 0 ? (
          <p>No apartments found for the specified county.</p>
        ) : (
          <div className="apartments-list">
            {apartments.map(apartment => (
              <div key={apartment.id} className="apartment-card">
                <h3>{apartment.address}</h3>
                <p>Bedrooms: {apartment.bedrooms}</p>
                <p>County: {apartment.county}</p>
                <p>Description: {apartment.description}</p>
                <img src={apartment.images} alt={`Apartment ${apartment.id}`} />
                <p>Price: ${apartment.price}</p>
                <p>Available: {apartment.is_available ? "Yes" : "No"}</p>
              </div>
            ))}
          </div>
        )}
      </div>
      <Footer />
    </div>
  );
  
};

export default Apartments;
