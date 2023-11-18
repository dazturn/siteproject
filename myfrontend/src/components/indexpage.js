import React, { useEffect, useState} from 'react';
import './index.css';
import axios from 'axios';

const Indexpage = () => {
  const [data, setData] = useState({ profiles: [], sml: [], images: [] });

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
      
      {/* Render profile(s) */}
      <div>
        {data.profiles.map((profile) => (
          <div key={profile.id}>
            <h2>{profile.owner_name}</h2>
            <p>{profile.owner_bio}</p>
            <p>Contact me Today: {profile.contact_info}</p>
          </div>
        ))}
      </div>

      {/* Render social media link(s) */}
      <div>
        {data.sml.map((socialMedia) => (
          <div key={socialMedia.id}>
            <p>Platform: {socialMedia.platform}</p>
            <p>URL: {socialMedia.url}</p>
            <img src={socialMedia.icon} alt="" />
          </div>
        ))}
      </div>

      {/* Render image(s) */}
      <div>
        {data.images.map((image) => (
          <div key={image.id}>
            <p>Image Title: {image.image_title}</p>
            <img src={image.image} alt="" />
          </div>
        ))}
      </div>
    </div>
  );
};  

export default Indexpage;