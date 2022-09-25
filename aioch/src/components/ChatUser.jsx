import React, { useState } from "react";
import MyButton from "./UI/button/MyButton";
import MyInput from "./UI/input/MyInput";
// import caller from '../caller/caller.js';

const Input = function (props) {
  let container = props.field.container;
  const setPost = props.field.setPost;

    const [message, setMessage] = useState('');

    const addNewMessage = () =>{
      container.addPost(props.field.name, message);
      setPost(container.getPosts());
    }

    return ( 
        <div className="input_field">
          <h1>{props.field.name}</h1>
          <MyInput 
            value = {message}
            onChange = {e => setMessage(e.target.value)}
            type='text' 
          />
          <MyButton onClick={addNewMessage}>Submit</MyButton>
        </div>
    );
}

export default Input;