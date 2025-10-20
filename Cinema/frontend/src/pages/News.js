import React from "react";

function News() {
  const articles = [
    { title: "New Marvel Movie Announced", date: "Oct 15, 2025" },
    { title: "Oscar Predictions: Top Contenders", date: "Oct 10, 2025" },
    { title: "Behind the Scenes of Dune 3", date: "Oct 5, 2025" },
  ];

  return (
    <section className="news">
      <h2>Latest News</h2>
      <div className="news-list">
        {articles.map((a, i) => (
          <article key={i} className="news-item">
            <h3>{a.title}</h3>
            <span>{a.date}</span>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </article>
        ))}
      </div>
    </section>
  );
}

export default News;
