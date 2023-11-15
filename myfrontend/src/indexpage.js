import React, { useEffect, useState} from 'react';
import './index.css';
import axios from 'axios';

const Indexpage = () => {
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
    <h1>Welcome to my Portfolio Homepage!</h1>
    {data.map((item) => (
      <div key={item.id}>
        <h2>{item.owner_name}</h2>
        <img src={item.image} alt="" />
        <p>{item.owner_bio}</p>
        <p>Contact me Today: {`${item.contact_info} ${item.platform}`}</p>
      </div>
    ))}
  </div>
  );
};

export default Indexpage;