import React, { useEffect, useState } from "react";
import "./Css/About.css";

function About() {
  const [aboutData, setAboutData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/about/")
      .then((res) => res.json())
      .then((data) => setAboutData(data))
      .catch((err) => console.error("Error fetching about data:", err));
  }, []);

  return (
    <div className="about-page">
      <h1>About Us</h1>
      {aboutData.map((item) => (
        <div key={item.id} className="about-card">
          <p className="description">{item.description}</p>
          <p>📍Address: {item.address}</p>
          <p>📧 Email: {item.email}</p>
          <p>📞 Phone: {item.phone}</p>
        </div>
      ))}
    </div>
  );
}

export default About;
