import React from 'react';
import LevelAccessLogo from '../assets/logo.png'
import './Navbar.scss'
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className='navbar'>
            <div>
                <Link to='/'><img src={LevelAccessLogo} alt="" className='navbar-logo' /></Link>
            </div>
        </nav>
    );
};

export default Navbar;