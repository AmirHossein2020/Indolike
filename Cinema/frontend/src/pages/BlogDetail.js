// src/pages/BlogDetail.js
import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import "./BlogDetail.css";

function BlogDetail() {
  const { blogId } = useParams();
  const navigate = useNavigate();
  const [blog, setBlog] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/blogs/${blogId}/`)
      .then((res) => res.json())
      .then((data) => {
        setBlog(data);
        setLoading(false);
      });
  }, [blogId]);

  if (loading) return <p>در حال بارگذاری بلاگ...</p>;
  if (!blog) return <p>بلاگ یافت نشد.</p>;

  return (
    <div className="blog-detail-container">
      <h1>{blog.name}</h1>
      <p>{blog.description}</p>
      <div className="post-grid">
        {blog.posts.map((p) => (
          <div key={p.id} className="post-card">
            <img
              src={p.image || "https://via.placeholder.com/200x120?text=No+Image"}
              alt={p.title}
            />
            <h3>{p.title}</h3>
            <p>{p.content.slice(0, 100)}...</p>
            <button onClick={() => navigate(`/post/${p.id}`)}>جزئیات پست</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default BlogDetail;
