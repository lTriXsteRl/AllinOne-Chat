import React, { useState } from "react";
import caller from '../caller/caller.js';

const Input = function (props) {
    const [value, setValue] = useState('Some Text');

    return ( 
        <div>
        <h1>{props.field.name}</h1>
        <input 
          type='text' 
          value={value}
          onChange={event => caller.setText(event.target.value)}
        />
        <button></button>
      </div>
    );
}

export default Input;