import React from "react";

function Movies() {
  const movieList = [
    { title: "Inception", year: 2010 },
    { title: "Interstellar", year: 2014 },
    { title: "The Dark Knight", year: 2008 },
  ];

  return (
    <section className="movies">
      <h2>Now Showing</h2>
      <div className="movie-grid">
        {movieList.map((m, i) => (
          <div key={i} className="movie-card">
            <div className="poster"></div>
            <h3>{m.title}</h3>
            <p>{m.year}</p>
            <button>Buy Ticket</button>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Movies;
