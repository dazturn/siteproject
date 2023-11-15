import React, { useEffect, useState} from 'react';
import './index.css';
import axios from 'axios';

const Aptitude = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

return (
  <div>
    <h1>Welcome to my Aptitude Page!</h1>
    {data.map((item) => (
      <div key={item.id}>
        <h2>{item.institution}</h2>
      </div>
    ))}
  </div>
  );
};

export default Aptitude;