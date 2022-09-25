import React, { useState } from "react";
import ChatHistory from "./components/ChatHistory";
import ChatUser from "./components/ChatUser";
import './styles/App.css'
import Container from "./Container";


let container = new Container();

function App() {
  const[posts, setPosts] = useState(container.getPosts());

  const createPost = (newPost) => {
    setPosts([...posts, newPost])
  }

  return (
    <div className="App">
        <div className="user_field">
          <ChatUser field={{name: "Костя"}} container={{container: container}} create={createPost}/>
          <ChatUser field={{name: "Влад"}} container={{container: container}} create={createPost}/>
        </div>
        <ChatHistory posts={posts}/>
    </div>
  );
}

export default App;
