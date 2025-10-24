import React, { useEffect, useState } from "react";
import "./Cart.css";

function Cart() {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    const savedCart = JSON.parse(localStorage.getItem("cart")) || [];
    console.log("🛒 Loaded cart:", savedCart);
    setCart(savedCart);
  }, []);

  const removeFromCart = (id) => {
    const updatedCart = cart.filter((item) => item.id !== id);
    setCart(updatedCart);
    localStorage.setItem("cart", JSON.stringify(updatedCart));
  };

  const totalPrice = cart.reduce((sum, item) => sum + Number(item.price || 0), 0);

  return (
    <div className="cart-container">
      <h1 className="page-title">🛍️ سبد خرید من</h1>

      {cart.length === 0 ? (
        <p className="empty-cart">سبد خرید شما خالی است 🛒</p>
      ) : (
        <>
          <div className="cart-grid">
            {cart.map((item, index) => (
              <div key={index} className="cart-card">
                <div className="cart-image-container">
                  <img
                    src={
                      item.movie?.image ||
                      "https://placehold.co/200x300?text=No+Image"
                    }
                    alt={item.movie?.name}
                    className="cart-image"
                  />
                </div>

                <div className="cart-details">
                  <h2 className="cart-title">{item.movie?.name}</h2>
                  <p className="cart-price">💰 {item.price} تومان</p>

                  <button
                    className="btn-remove"
                    onClick={() => removeFromCart(item.id)}
                  >
                    ❌ حذف از سبد
                  </button>
                </div>
              </div>
            ))}
          </div>

          <div className="cart-summary">
            <h3>جمع کل: {totalPrice.toLocaleString()} تومان</h3>
            <button className="btn-pay">💳 پرداخت</button>
          </div>
        </>
      )}
    </div>
  );
}

export default Cart;
