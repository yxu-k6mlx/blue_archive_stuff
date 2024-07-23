import React from 'react';
import ReactDOM from 'react-dom';

const AUTO = "AUTO" 
const MENU = "MENU"

function AutoButton() {
    return (
        <Image 
            src="auto.svg"
            alt="AUTO"
            priority
        />
    ); 
}

function MenuButton() {
    return (
        <Image 
            src="menu.svg"
            alt="MENU"
            priority
        />
    ); 
}

// UI Button was from https://github.com/ArisStudio/ArisStudio_Legacy/blob/0.3.0.ArisStudio/Assets/ArisStudio/AsGameObject/Components/Button/UI_Button.png
