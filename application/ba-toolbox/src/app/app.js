import React from 'react';
import ReactDOM from 'react-dom';

import BA_Button from "./modules/media_controls/buttons"

export default function Application() {
    return (
        <div>
            <BA_Button button_text={"auto"} /> <BA_Button button_text={"menu"} /> 
        </div>
    ); 
}