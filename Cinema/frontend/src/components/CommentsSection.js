// src/components/CommentsSection.js
import React, { useState } from "react";
import "./CommentsSection.css";

export default function CommentsSection({ comments, postId, onNewComment }) {
  const [commentContent, setCommentContent] = useState("");

  const handleCommentSubmit = async () => {
    if (!commentContent.trim()) return;

    const token = localStorage.getItem("accessToken");
    if (!token) {
      alert("لطفاً ابتدا وارد شوید.");
      return;
    }

    try {
      const res = await fetch(`http://127.0.0.1:8000/api/posts/${postId}/comment/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ content: commentContent }),
      });

      if (!res.ok) throw new Error("Failed to post comment");

      const newComment = await res.json();
      onNewComment(newComment);
      setCommentContent("");
    } catch (err) {
      console.error(err);
      alert("❌ ارسال کامنت موفق نبود!");
    }
  };

  return (
    <div className="comments-section">
      <h3>💬 نظرات کاربران</h3>

      <div className="comment-form">
        <textarea
          placeholder="نظر خود را وارد کنید..."
          value={commentContent}
          onChange={(e) => setCommentContent(e.target.value)}
        />
        <button onClick={handleCommentSubmit}>ارسال نظر</button>
      </div>

      <div className="comments-list">
        {comments.length === 0 && <p>هیچ نظری ثبت نشده است.</p>}
        {comments.map((c) => (
          <div key={c.id} className="comment-card">
            <div className="comment-header">
              <span className="comment-user">{c.user.username}</span>
              <span className="comment-date">
                {new Date(c.date_created).toLocaleString()}
              </span>
            </div>
            <p className="comment-content">{c.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
