import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [sustainabilityData, setSustainabilityData] = useState([]);
  const [christmasData, setChristmasData] = useState([]);

  useEffect(() => {
    // Fetch sustainability data
    axios.get('http://127.0.0.1:8000/sustainability')
      .then(response => {
        setSustainabilityData(response.data);
      })
      .catch(error => {
        console.error('Error fetching sustainability data:', error);
      });

    // Fetch Christmas data
    axios.get('http://127.0.0.1:8000/christmas')
      .then(response => {
        setChristmasData(response.data);
      })
      .catch(error => {
        console.error('Error fetching Christmas data:', error);
      });
  }, []);

  return (
    <div>
      <h1>RAG Survey Analysis Tool</h1>

      <h2>Sustainability Data</h2>
      <pre>{JSON.stringify(sustainabilityData, null, 2)}</pre>

      <h2>Christmas Data</h2>
      <pre>{JSON.stringify(christmasData, null, 2)}</pre>
    </div>
  );
}

export default App;

