import React, { useEffect, useState} from 'react';
import './index.css';
import App from './App';
import axios from 'axios';

const Projects = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/projects');
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

return (
  <div>
    <App />
    <h1>Welcome to my Project Page!</h1>
    {data.map((item) => (
      <div key={item.id}>
        <h2>{item.pg_title}</h2>
        <h3>{item.date_completed}</h3>
        <p>{item.pj_description}</p>
        <p>Contact me Today: {`${item.contact_info} ${item.platform}`}</p>
      </div>
    ))}
  </div>
  );
};

export default Projects;