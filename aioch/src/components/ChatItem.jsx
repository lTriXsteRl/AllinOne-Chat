import React from 'react';

function ChatItem(props) {
    return ( 
        <div className='chat__item'>
            {/* <p>{props.post.id}</p> */}
            {/* <p>|</p> */}
            <h3>{props.post.user}</h3>
            <p>|</p>
            <p>{props.post.body}</p>
        </div>
     );
}

export default ChatItem;