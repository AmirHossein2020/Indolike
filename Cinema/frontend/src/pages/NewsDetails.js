import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./NewsDetails.css";

function NewsDetails() {
  const { blogId } = useParams();
  const [blog, setBlog] = useState(null);
  const [posts, setPosts] = useState([]);
  const [comments, setComments] = useState([]);
  const [commentText, setCommentText] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const token = localStorage.getItem("accessToken");

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch blog details
        const blogRes = await fetch(`http://127.0.0.1:8000/api/blogs/${blogId}/`);
        const blogData = await blogRes.json();
        setBlog(blogData);

        // Fetch posts
        const postsRes = await fetch(`http://127.0.0.1:8000/api/posts/?blog=${blogId}`);
        const postsData = await postsRes.json();
        setPosts(postsData);

        // Fetch comments
        const commentsRes = await fetch(`http://127.0.0.1:8000/api/posts/${blogId}/comments/`);
        const commentsData = await commentsRes.json();
        setComments(commentsData);
      } catch (err) {
        console.error("Error fetching blog details:", err);
        setError("خطا در دریافت اطلاعات از سرور");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [blogId]);

  // ارسال کامنت جدید
  async function handleCommentSubmit(e) {
    e.preventDefault();
    if (!token) {
      alert("لطفا ابتدا وارد شوید.");
      return;
    }
    if (!commentText.trim()) return;

    try {
      const res = await fetch(`http://127.0.0.1:8000/api/posts/${blogId}/comment/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ content: commentText }),
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || "خطا در ارسال نظر");
      }

      const newComment = await res.json();
      setComments((prev) => [...prev, newComment]);
      setCommentText("");
    } catch (err) {
      alert(err.message);
    }
  }

  if (loading) return <p className="loading">در حال بارگذاری...</p>;
  if (error) return <p className="error">{error}</p>;
  if (!blog) return <p>خبر پیدا نشد.</p>;

  return (
    <div className="news-details">
      {/* --- Blog Section --- */}
      <div className="blog-header">
        <img
          src={blog.image || "https://via.placeholder.com/600x300?text=No+Image"}
          alt={blog.name}
          className="blog-image"
        />
        <div className="blog-content">
          <h1>{blog.name}</h1>
          <p>{blog.description}</p>
        </div>
      </div>

      
      {/* --- Related Posts --- */}
        <div className="posts-section">
        <h2>🎬 پست‌های مرتبط</h2>
        <div className="posts-grid">
            {posts.length === 0 ? (
            <p className="no-posts">پستی برای این خبر وجود ندارد.</p>
            ) : (
            posts.map((post) => (
                <div className="post-card adaptive" key={post.id}>
                <div className="post-image-container">
                    <img
                    src={post.image || "https://via.placeholder.com/400x300?text=No+Image"}
                    alt={post.title}
                    className="adaptive-img"
                    loading="lazy"
                    />
                </div>
                <div className="post-content-box">
                    <h3>{post.title}</h3>
                    <p>{post.content.slice(0, 120)}...</p>
                </div>
                </div>
            ))
            )}
        </div>
        </div>

      {/* --- Comments Section --- */}
      <div className="comments-section">
        <h2>💬 بخش نظرات</h2>

        {token ? (
          <form onSubmit={handleCommentSubmit} className="comment-form">
            <textarea
              value={commentText}
              onChange={(e) => setCommentText(e.target.value)}
              placeholder="نظر خود را بنویسید..."
              required
            />
            <button type="submit" className="btn-submit">
              ارسال نظر
            </button>
          </form>
        ) : (
          <p className="login-alert">برای ارسال نظر ابتدا وارد شوید.</p>
        )}

        <div className="comments-list">
          {comments.length === 0 ? (
            <p>نظری برای این خبر ثبت نشده است.</p>
          ) : (
            comments.map((c) => (
              <div className="comment-card" key={c.id}>
                <div className="comment-header">
                  <strong>{c.username || "کاربر ناشناس"}</strong>
                  <span className="comment-date">
                    {c.date_created
                      ? new Date(c.date_created).toLocaleString("fa-IR")
                      : ""}
                  </span>
                </div>
                <p className="comment-content">{c.content}</p>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default NewsDetails;
