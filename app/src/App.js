import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react';


function App() {
  const [hashtags, setHashtags] = useState('')

  const getHashtags = (sentence) => {
    async function getBackend() {
      const res = await fetch('http://localhost:5000/gethashtags', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json' ,
        },
        body: JSON.stringify(sentence),
        mode: 'cors'
      }
      )
    }
  }

  return (
    <div className="App">
      <h1>UI for IP-Crowd</h1>
      <input type='text' placeholder='Enter a Sentence' ></input>
      <p>{hashtags}</p>
    </div>
  );
}

export default App;
