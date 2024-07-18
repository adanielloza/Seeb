// src/components/SubmitButton.jsx
import React from 'react';

const SubmitButton = ({ onClick, label }) => {
    return (
        <button onClick={onClick} type="button">
            {label}
        </button>
    );
};

export default SubmitButton;
