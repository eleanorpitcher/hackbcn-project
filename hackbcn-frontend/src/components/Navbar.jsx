import React from 'react';
import LevelAccessLogo from '../assets/logo.png'

const Navbar = () => {
    return (
        <nav style={{display:'flex', width: '100%', margin: '0'}}>
            <div>
                <img src={LevelAccessLogo} alt="" style={{width:'20%'}} />
            </div>
        </nav>
    );
};

export default Navbar;