import React, { useState, useEffect } from 'react';
import './Homepage.scss'; // Assuming you have a separate SCSS file for styling
import LogoL from '../assets/logo-L.png';

function Homepage() {
  const locations = ['Barcelona', 'London', 'Paris'];

  const [inputValue, setInputValue] = useState('');
  const [filteredLocations, setFilteredLocations] = useState([]);
  const [showDropdown, setShowDropdown] = useState(false);

  const handleInputChange = (event) => {
    const value = event.target.value.toLowerCase();
    setInputValue(value);

    // Filter locations based on input value
    const filtered = locations.filter(location =>
      location.toLowerCase().includes(value)
    );

    setFilteredLocations(filtered);
    setShowDropdown(true); // Show dropdown when filtering starts
  };

  const handleSelectLocation = (location) => {
    setInputValue(location);
    setShowDropdown(false); // Hide dropdown after selecting a location
  };

  const handleOutsideClick = (event) => {
    if (!event.target.closest('.search_bar_container')) {
      setShowDropdown(false); // Close dropdown if clicked outside
    }
  };

  // Event listener to close dropdown when clicking outside
  useEffect(() => {
    document.addEventListener('mousedown', handleOutsideClick);
    return () => {
      document.removeEventListener('mousedown', handleOutsideClick);
    };
  }, []);

  return (
    <div className='homepage-container'>
      <div className='header_container'>
        <div className='h1'>
          <img src={LogoL} alt="Logo" className='logo-image-header' />
          <h1 className='header'>evel Access for Everyone</h1>
        </div>
        <h2 className='second_header'>Find accessible locations around the city</h2>
      </div>

      <div className='search_bar_container'>
        <form action="" className='form'>
          <input
            type="text"
            placeholder="Search..."
            className='input'
            value={inputValue}
            onChange={handleInputChange}
          />
          {showDropdown && (
            <div className="dropdown_content">
              {filteredLocations.length > 0 ? (
                filteredLocations.map((location, index) => (
                  <div
                    key={index}
                    className="dropdown_item"
                    onClick={() => handleSelectLocation(location)}
                  >
                    {location}
                  </div>
                ))
              ) : (
                <div className="dropdown_item">No results found</div>
              )}
            </div>
          )}
          <button className='button_container'>Search</button>
        </form>
      </div>

      <div className='section_two'>
        <h2 className='third_header'>The most accessible locations in Barcelona</h2>
        <div className='location_cards'>
          <div className='individual_card'>
            <h3>Location 1</h3>
            <img src="" alt="Location 1" />
          </div>
          <div className='individual_card'>
            <h3>Location 2</h3>
            <img src="" alt="Location 2" />
          </div>
          <div className='individual_card'>
            <h3>Location 3</h3>
            <img src="" alt="Location 3" />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Homepage;
