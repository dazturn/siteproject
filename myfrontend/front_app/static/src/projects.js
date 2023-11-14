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

  </div>
  );
};

export default Projects;