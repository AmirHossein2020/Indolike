import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./CartPage.css";

function CartPage() {
  const [cart, setCart] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  const token = localStorage.getItem("accessToken");

  useEffect(() => {
    if (!token) {
      navigate("/login");
      return;
    }

    fetch("http://127.0.0.1:8000/api/cart/", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => {
        setCart(data);
        setLoading(false);
      });
  }, [navigate, token]);

  const removeFromCart = (movieId) => {
    fetch(`http://127.0.0.1:8000/api/cart/remove/${movieId}/`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` },
    }).then(() => {
      setCart(cart.filter((item) => item.online_movie !== movieId));
    });
  };

  const handleCheckout = () => {
    fetch("http://127.0.0.1:8000/api/cart/checkout/", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => {
        alert(data.detail);
        navigate("/online-movies");
      });
  };

  if (loading) return <p>Loading cart...</p>;

  return (
    <div className="cart-container">
      <h2>🛒 Your Cart</h2>
      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          <div className="cart-items">
            {cart.map((item) => (
              <div key={item.id} className="cart-item">
                <img src={item.image} alt={item.movie_name} />
                <div>
                  <h3>{item.movie_name}</h3>
                  <p>💰 ${item.price}</p>
                </div>
                <button onClick={() => removeFromCart(item.online_movie)}>
                  ❌ Remove
                </button>
              </div>
            ))}
          </div>

          <button className="checkout-btn" onClick={handleCheckout}>
            ✅ Checkout & Buy All
          </button>
        </>
      )}
    </div>
  );
}

export default CartPage;
