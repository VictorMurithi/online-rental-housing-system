import React from "react";
import "../App.css";

function Landing() {
  return (
    <div className="container">
      <div id="renters" className="section">
        <div className="search guide">
          <h2>For Renters</h2>
          <hr />
          <h1>Let our search guide you</h1>
          <p>
            Search thousands of up-to-date property listings on our easy-to-use
            website. Narrow down your options by choosing what's most important
            to you, such as price range, location, and more. Parents can also
            search for rentals that fall within a particular school.
          </p>
          <button>start my search</button>
        </div>
      </div>

      <div className="landlords section" id="landlordslayout">
        <h2>For Landlords</h2>
        <hr />
        <h1>Simple and streamlined rental management all under a single roof</h1>
        <div className="listingproperty" id="listingproperty1">
          <div className="listingcontainer">
            <div className="imgcontainer">
              <img
                src="./Images/istockphoto-643897728-2048x2048.jpg"
                alt="Loading image"
              />
            </div>
            <div className="textcontainer">
              <h3>List your rental property</h3>
              <p>
                Post your rental property in minutes to reach millions of
                potential renters.
              </p>
              <button>Add Listing</button>
            </div>
          </div>
        </div>

        <div className="listingproperty" id="listingproperty2">
          <div className="listingcontainer">
            <div className="textcontainer">
              <h3>Screen potential clients</h3>
              <p>
                Completed applications and reports are generated instantly and
                immediately shared with landlords, drastically reducing cycle
                times and empowering renters to receive a decision in hours
                instead of days.
              </p>
              <button>screen tenants</button>
            </div>
            <div className="imgcontainer">
              <img
                src="./Images/pexels-photo-5668858.webp"
                alt="Loading image"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Landing;
