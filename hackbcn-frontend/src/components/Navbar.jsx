import React from 'react';
import LevelAccessLogo from '../assets/logo.png'
import './Navbar.scss'

const Navbar = () => {
    return (
        <nav className='navbar'>
            <div>
                <img src={LevelAccessLogo} alt="" className='navbar-logo' />
            </div>
        </nav>
    );
};

export default Navbar;