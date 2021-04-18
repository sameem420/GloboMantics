import React from 'react';
import GlobalLogo from '../assets/images/GloboLogo.png';
import './styles.css';

function Header(props) {
    return (
        <div className="row">
            <div className="col-md-5">
                <img src={GlobalLogo} className="logo" alt="Globomantics Logo" />
            </div>
            <div className="col-md-7 mt-5 subtitle">
                {props.subtitle}
            </div>
        </div>
    );
}

export default Header;