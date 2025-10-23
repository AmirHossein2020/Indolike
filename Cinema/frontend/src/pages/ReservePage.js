import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import "./ReservePage.css";

function ReservePage() {
  const { showtimeId } = useParams();
  const navigate = useNavigate();

  const [seats, setSeats] = useState([]);
  const [selectedSeat, setSelectedSeat] = useState(null);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState("");

  const token = localStorage.getItem("accessToken");

  useEffect(() => {
    const fetchSeats = async () => {
      setLoading(true);
      setErrorMsg("");

      if (!showtimeId) {
        setErrorMsg("No showtimeId in URL.");
        setLoading(false);
        return;
      }

      if (!token) {
        navigate("/login");
        return;
      }

      try {
        const res = await fetch(
          `http://127.0.0.1:8000/api/showtimes/${showtimeId}/seats/`,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (!res.ok) {
          setErrorMsg(`Failed to fetch seats: ${res.status}`);
          setSeats([]);
          setLoading(false);
          return;
        }

        const data = await res.json();
        setSeats(Array.isArray(data) ? data : data.results || []);
      } catch (err) {
        setErrorMsg("Network error while fetching seats.");
        console.error(err);
        setSeats([]);
      } finally {
        setLoading(false);
      }
    };

    fetchSeats();
  }, [showtimeId, token, navigate]);

  const handleReserve = async () => {
    if (!selectedSeat) {
      alert("Please select a seat.");
      return;
    }

    if (!token) {
      navigate("/login");
      return;
    }

    try {
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

      if (!res.ok) {
        alert(`❌ Reservation failed: ${data.detail || res.status}`);
        return;
      }

      setSeats((prevSeats) =>
        prevSeats.map((seat) =>
          seat.id === selectedSeat ? { ...seat, is_reserved: true } : seat
        )
      );
      setSelectedSeat(null);
      alert("✅ Seat reserved successfully!");
    } catch (err) {
      console.error(err);
      alert("Reservation failed due to network error.");
    }
  };

  if (loading) return <p>Loading seats...</p>;

  return (
    <div className="reserve-container">
      <h2>Select Your Seat</h2>
      {errorMsg && <p style={{ color: "crimson" }}>{errorMsg}</p>}

      <div className="seat-grid">
        {seats.length === 0 ? (
          <p>No seats available.</p>
        ) : (
          seats.map((seat) => (
            <div
              key={seat.id}
              className={`seat ${
                seat.is_reserved ? "reserved" : ""
              } ${selectedSeat === seat.id ? "selected" : ""}`}
              onClick={() => !seat.is_reserved && setSelectedSeat(seat.id)}
            >
              {seat.row}-{seat.number}
            </div>
          ))
        )}
      </div>

      <button
        onClick={handleReserve}
        disabled={!selectedSeat}
        className="reserve-btn"
      >
        Reserve Selected Seat
      </button>
    </div>
  );
}

export default ReservePage;
