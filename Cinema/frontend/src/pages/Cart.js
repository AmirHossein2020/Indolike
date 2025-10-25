import React, { useEffect, useState } from "react";
import "./Cart.css";

function Cart() {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    const savedCart = JSON.parse(localStorage.getItem("cart")) || [];
    setCart(savedCart);
  }, []);

  const updateCart = (newCart) => {
    setCart(newCart);
    localStorage.setItem("cart", JSON.stringify(newCart));
  };

  const increaseQuantity = (id) => {
    const updated = cart.map((item) =>
      item.id === id ? { ...item, quantity: (item.quantity || 1) + 1 } : item
    );
    updateCart(updated);
  };

  const decreaseQuantity = (id) => {
    const updated = cart
      .map((item) =>
        item.id === id && (item.quantity || 1) > 1
          ? { ...item, quantity: item.quantity - 1 }
          : item
      )
      .filter((item) => (item.quantity || 1) > 0);
    updateCart(updated);
  };

  const removeFromCart = (id) => {
    const updated = cart.filter((item) => item.id !== id);
    updateCart(updated);
  };

  const totalPrice = cart.reduce(
    (sum, item) => sum + Number(item.price || 0) * (item.quantity || 1),
    0
  );

  if (cart.length === 0) {
    return (
      <div className="cart-container">
        <h1>🛒 سبد خرید شما خالی است</h1>
      </div>
    );
  }

  return (
    <div className="cart-container">
      <h1 className="page-title">🛒 سبد خرید من</h1>
      <div className="cart-grid">
        {cart.map((item) => (
          <div key={item.id} className="cart-card">
            <div className="cart-image">
              <img
                src={
                  item.movie?.image ||
                  "https://placehold.co/200x300?text=No+Image"
                }
                alt={item.movie?.name}
              />
            </div>
            <div className="cart-details">
              <h2>{item.movie?.name}</h2>
              <p>💰 قیمت: {item.price.toLocaleString()} تومان</p>
              <div className="quantity-controls">
                <button onClick={() => decreaseQuantity(item.id)}>➖</button>
                <span>{item.quantity || 1}</span>
                <button onClick={() => increaseQuantity(item.id)}>➕</button>
              </div>
              <button
                className="btn-remove"
                onClick={() => removeFromCart(item.id)}
              >
                حذف
              </button>
            </div>
          </div>
        ))}
      </div>
      <div className="cart-summary">
        <h2>جمع کل: {totalPrice.toLocaleString()} تومان</h2>
        <button className="btn-pay">💳 پرداخت</button>
      </div>
    </div>
  );
}

export default Cart;
