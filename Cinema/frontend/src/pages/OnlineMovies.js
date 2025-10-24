import React, { useEffect, useState } from "react";
import "./Home.css"; // از همون استایل کارت‌های Home استفاده می‌کنیم

function OnlineMovies() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/online-movies/")
      .then((res) => res.json())
      .then((data) => {
        setMovies(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching online movies:", err);
        setLoading(false);
      });
  }, []);

  const addToCart = (movie) => {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    const exists = cart.find((item) => item.id === movie.id);
    if (exists) {
      alert("✅ این فیلم قبلاً در سبد خرید شماست!");
      return;
    }
    cart.push(movie);
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("🛒 فیلم به سبد خرید افزوده شد!");
  };

  if (loading) return <p className="loading">در حال بارگذاری فیلم‌ها...</p>;

  if (movies.length === 0)
    return <p className="loading">فیلم آنلاینی در دسترس نیست.</p>;

  return (
    <div className="home-container">
      <h1 className="page-title">🎬 فیلم‌های آنلاین برای خرید</h1>

      <div className="movie-grid">
        {movies.map((item) => (
          <div key={item.id} className="movie-card">
            <div className="movie-image-container">
              <img
                src={item.movie?.image}
                alt={item.movie?.name}
                className="movie-image"
              />
            </div>

            <div className="movie-info">
              <h2 className="movie-title">{item.movie?.name}</h2>
              <p className="movie-description">
                {item.movie?.description?.length > 80
                  ? item.movie.description.slice(0, 80) + "..."
                  : item.movie?.description}
              </p>
              <p className="movie-meta">💰 قیمت: {item.price} تومان</p>

              <button
                className="btn-reserve"
                onClick={() => addToCart(item)}
              >
                🛒 افزودن به سبد خرید
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default OnlineMovies;
