import React from 'react';
import ChatItem from './ChatItem';

function ChatHistory({posts}) {
    return ( 
    <div className='chat__history'>
        {posts.map((post) => 
          <ChatItem post={post} key={post.id}/>
        )}
    </div> );
}

export default ChatHistory;