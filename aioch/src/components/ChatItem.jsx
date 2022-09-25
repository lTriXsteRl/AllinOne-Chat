import React from 'react';

function ChatItem(props) {
    let date = props.post.id.toString();

    return ( 
        <div className='chat__item'>
            <p>{date.substring(0,2)} : {date.substring(3,5)}</p>
            <p>|</p> 
            <h3>{props.post.user}</h3>
            <p>|</p>
            <p>{props.post.body}</p>
        </div>
     );
}

export default ChatItem;