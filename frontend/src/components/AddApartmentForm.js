// AddApartmentForm.js
import React, { useState } from "react";
import Navbar from "../layout/Navbar";
import Footer from "../layout/Footer";
import "../App.css";

export default function AddApartmentForm() {
    const [description, setDescription] = useState("");
    const [county, setCounty] = useState("");
    const [price, setPrice] = useState("");
    const [images, setImages] = useState([]);

    const handleSubmit = (event) => {
        event.preventDefault();
        // Here you can handle form submission, e.g., send data to backend
        console.log("Form submitted:", { description, county, price, images });
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
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                        ></textarea>
                    </div>
                    <div className="form-group">
                        <label htmlFor="county">County:</label>
                        <input
                            type="text"
                            className="form-control"
                            id="county"
                            value={county}
                            onChange={(e) => setCounty(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="price">Price:</label>
                        <input
                            type="text"
                            className="form-control"
                            id="price"
                            value={price}
                            onChange={(e) => setPrice(e.target.value)}
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="images">Apartment Images:</label>
                        <input
                            type="file"
                            className="form-control-file"
                            id="images"
                            multiple
                            onChange={(e) => setImages(e.target.files)}
                        />
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
