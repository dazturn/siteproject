import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
    return (
        <nav>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/aptitude"></Link>
                </li>
                <li>
                    <Link to="/projects"></Link>
                </li>
            </ul>
        </nav>
    );
};

export default NavBar;