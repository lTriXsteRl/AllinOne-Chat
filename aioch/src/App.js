import React, { useState } from "react";
import ChatHistory from "./components/ChatHistory";
import ChatUser from "./components/ChatUser";
import './styles/App.css'
import Container from "./Container";


let container = new Container();

function App() {
  const[posts, setPosts] = useState(container.getPosts());

  return (
    <div className="App">
        <div className="user_field">
          <ChatUser field={{name: "Костя", container: container, setPost: setPosts}}/>
          <ChatUser field={{name: "Влад", container: container}}/>
        </div>
        <ChatHistory posts={posts}/>
    </div>
  );
}

export default App;
