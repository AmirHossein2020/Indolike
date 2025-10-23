import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./ReservePage.css";

function ReservePage() {
  const { showtimeId } = useParams();
  const [seats, setSeats] = useState([]);
  const [selectedSeat, setSelectedSeat] = useState(null);
  const [loading, setLoading] = useState(true);

  const token = localStorage.getItem("accessToken");

  // Fetch seats
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/showtimes/${showtimeId}/seats/`)
      .then((res) => res.json())
      .then((data) => {
        setSeats(data);
        setLoading(false);
      })
      .catch((err) => console.error(err));
  }, [showtimeId]);

  // Handle reservation
  async function handleReserve() {
    if (!selectedSeat) return;
    if (!token) {
      alert("Please log in first!");
      window.location.href = "/login";
      return;
    }

    const res = await fetch("http://127.0.0.1:8000/api/reserve-seat/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        showtime_id: showtimeId,
        seat_id: selectedSeat,
      }),
    });

    const data = await res.json();

    if (res.ok) {
      alert("✅ Seat reserved successfully!");
      setSeats((prevSeats) =>
        prevSeats.map((seat) =>
          seat.id === selectedSeat ? { ...seat, is_reserved: true } : seat
        )
      );
      setSelectedSeat(null);
    } else {
      alert(`❌ Reservation failed: ${data.detail}`);
    }
  }

  if (loading) return <p>Loading seats...</p>;

  return (
    <div className="reserve-container">
      <h2>Select Your Seat</h2>
      <div className="seat-grid">
        {seats.map((seat) => (
          <div
            key={seat.id}
            className={`seat ${seat.is_reserved ? "reserved" : ""} ${
              selectedSeat === seat.id ? "selected" : ""
            }`}
            onClick={() => !seat.is_reserved && setSelectedSeat(seat.id)}
          >
            {seat.row}-{seat.number}
          </div>
        ))}
      </div>
      <button onClick={handleReserve} disabled={!selectedSeat}>
        Reserve Selected Seat
      </button>
    </div>
  );
}

export default ReservePage;
