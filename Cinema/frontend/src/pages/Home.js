import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Css/Home.css"; 

function Home() {
  const [showtimes, setShowtimes] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate(); 

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/showtimes/")
      .then((res) => res.json())
      .then((data) => {
        setShowtimes(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching showtimes:", err);
        setLoading(false);
      });
  }, []);

  const handleReserve = (showtimeId) => {
    const token = localStorage.getItem("accessToken");
    if (!token) {
      alert("Please log in first!");
      navigate("/login");
      return;
    }
    navigate(`/reserve/${showtimeId}`);
  };

  if (loading) {
    return <p className="loading">Loading movies...</p>;
  }

  if (showtimes.length === 0) {
    return <p className="loading">No showtimes available.</p>;
  }

  return (
    <div className="home-container">
      <h1 className="page-title">🎬 Now Showing in Cinemas</h1>

      <div className="movie-grid">
        {showtimes.map((item) => (
          <div key={item.id} className="movie-card">
            <div className="movie-image-container">
              <img
                src={item.movie.image}
                alt={item.movie.name}
                className="movie-image"
              />
            </div>

            <div className="movie-info">
              <h2 className="movie-title">{item.movie.name}</h2>
              <p className="movie-description">
                {item.movie.description.length > 80
                  ? item.movie.description.slice(0, 80) + "..."
                  : item.movie.description}
              </p>
              <p className="movie-meta">
                🎟 {item.hall.name} | 🕒{" "}
                {new Date(item.start_time).toLocaleTimeString([], {
                  hour: "2-digit",
                  minute: "2-digit",
                })}
              </p>
              <button
                className="btn-reserve"
                onClick={() => handleReserve(item.id)}
              >
                Reserve Seat
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
