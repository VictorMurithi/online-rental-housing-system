import React, { useState } from "react";
import Navbar from "../layout/Navbar";
import Footer from "../layout/Footer";
import "../App.css";

export default function AddApartmentForm() {
    const [apartment, setApartment] = useState({
        description: "",
        county: "",
        price: "",
        images: [],
        is_available: true
    });

    const handleSubmit = (event) => {
        event.preventDefault();
        // Here you can handle form submission, e.g., send data to backend
        console.log("Form submitted:", apartment);
    };

    return (
        <div>
            <Navbar />
            <div className="add-container-form">
                <h1 className="text-center mt-5">Add Apartment Listing</h1>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="description">Apartment Description:</label>
                        <textarea
                            className="form-control"
                            id="description"
                            rows="4"
                            value={apartment.description}
                            onChange={(e) => setApartment({ ...apartment, description: e.target.value })}
                        ></textarea>
                    </div>
                    <div className="form-group">
                        <label htmlFor="bedrooms">Bedrooms:</label>
                        <textarea
                            type="number"
                            className="form-control"
                            id="bedrooms"
                            value={apartment.bedrooms}
                            onChange={(e) => setApartment({ ...apartment, bedrooms: e.target.value })}
                        ></textarea>
                    </div>
                    <div className="form-group">
                        <label htmlFor="county">County:</label>
                        <input
                            type="text"
                            className="form-control"
                            id="county"
                            value={apartment.county}
                            onChange={(e) => setApartment({ ...apartment, county: e.target.value })}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="price">Price:</label>
                        <input
                            type="text"
                            className="form-control"
                            id="price"
                            value={apartment.price}
                            onChange={(e) => setApartment({ ...apartment, price: e.target.value })}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="images">Apartment Images:</label>
                        <input
                            type="file"
                            className="form-control-file"
                            id="images"
                            multiple
                            onChange={(e) => setApartment({ ...apartment, images: e.target.files })}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="is_available">Available:</label>
                        <select
                            className="form-control"
                            id="is_available"
                            value={apartment.is_available}
                            onChange={(e) => setApartment({ ...apartment, is_available: e.target.value })}
                        >
                            <option value={true}>Yes</option>
                            <option value={false}>No</option>
                        </select>
                    </div>
                    <button type="submit" className="btn btn-primary btn-block">
                        Submit
                    </button>
                </form>
            </div>
            <Footer />
        </div>
    );
}
