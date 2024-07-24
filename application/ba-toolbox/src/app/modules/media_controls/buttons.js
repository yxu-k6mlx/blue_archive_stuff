import React from 'react';
import styles from "./buttons.css"

export default function MediaButtons({button_text}) {
    return(
        <div className="ba_button_container">
            <div>
                <img src="https://github.com/ArisStudio/ArisStudio_Legacy/blob/0.3.0.ArisStudio/Assets/ArisStudio/AsGameObject/Components/Button/UI_Button.png?raw=true" alt={"raw text: " + button_text}/>
            </div>
            <div className="ba_button_text">
                <p>{button_text}</p>
            </div>
        </div>
    ); 
}

// UI Button was from https://github.com/ArisStudio/ArisStudio_Legacy/blob/0.3.0.ArisStudio/Assets/ArisStudio/AsGameObject/Components/Button/UI_Button.png
