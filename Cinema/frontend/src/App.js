import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import Movies from "./pages/Movies";
import News from "./pages/News";
import About from "./pages/About";
import ReservePage from "./pages/ReservePage";
import Login from "./pages/Login";
import Register from "./pages/Register";
import "./App.css";
import OnlineMovies from "./pages/OnlineMovies";
import Cart from "./pages/Cart";
import NewsDetails from "./pages/NewsDetails";
import Contact from "./pages/Contact";




function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <main className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/movies" element={<Movies />} />
            <Route path="/news" element={<News />} />
            <Route path="/news/:blogId" element={<NewsDetails />} />
            <Route path="/about" element={<About />} />
            <Route path="/reserve/:showtimeId" element={<ReservePage />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/online-movies" element={<OnlineMovies />} />
            <Route path="/cart" element={<Cart />} />



          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
