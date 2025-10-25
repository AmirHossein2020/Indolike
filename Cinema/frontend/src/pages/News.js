import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Css/News.css";

function News() {
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/blogs/")
      .then((res) => res.json())
      .then((data) => {
        setBlogs(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching blogs:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading news...</p>;
  if (blogs.length === 0) return <p>There is no news available.</p>;

  return (
    <div className="news-container">
      <h1 className="page-title">📰Latest news and articles</h1>
      <div className="blog-grid">
        {blogs.map((blog) => (
          <div key={blog.id} className="blog-card">
            <div className="blog-image-container">
              <img
                src={blog.image || "https://via.placeholder.com/200x120?text=No+Image"}
                alt={blog.name}
                className="blog-image"
              />
            </div>
            <div className="blog-info">
              <h2 className="blog-title">{blog.name}</h2>
              <p className="blog-description">
                {blog.description.length > 100
                  ? blog.description.slice(0, 100) + "..."
                  : blog.description}
              </p>
              <button
                className="btn-details"
                onClick={() => navigate(`/news/${blog.id}`)}
              >
                Details
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default News;
