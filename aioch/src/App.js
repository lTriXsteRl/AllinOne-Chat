import React, { useState } from "react";
import Input from "./components/Input";

function App() {
  

  return (
    <div className="App">
      <Input field={{name: "Костя"}}/>
      <Input field={{name: "Влад"}}/>
    </div>
  );
}

export default App;
