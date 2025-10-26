# 🎬 Cinema — Movie Ticket & Streaming Platform

A full-featured web application for **buying movie tickets**, **streaming online films**, and **reading movie news**,  
built with **React (Frontend)** and **Django REST Framework (Backend)**.

---

## 🚀 Overview

**Cinema** combines the functionality of an **online cinema ticket booking system**, an **e-commerce movie platform**, and a **movie blog** — all in one place.

Users can browse and purchase online movies, book cinema seats, read the latest movie news, and comment on posts.  
All features are secured with a full authentication system.

---

## 🧩 Core Features

### 🧑‍💻 User Authentication System
- User registration (Sign up)
- Login / Logout functionality
- JWT authentication for secure API communication
- Required login before booking tickets or making purchases

---

### 🎞 Online Movie Store (E-commerce)
- Browse available online movies for purchase or streaming  
- Add or remove movies from the **shopping cart**  
- View total price and manage items before checkout  
- Secure checkout flow through REST APIs  
- Fully connected with authenticated user accounts  

---

### 🎟 Event Tickets Booking System
- Book seats for cinema screenings  
- Seat availability handled dynamically through the backend  
- Only authenticated users can book or cancel tickets  
- Admin can manage movies, events, and bookings from Django Admin panel  

---

### 📰 RESTful Blog & News API
- Movie news and articles managed through a RESTful API  
- Each post includes a title, image, content, and publication date  
- Users can view post details and leave comments after logging in  
- Supports CRUD operations for admins (create, edit, delete posts)  

---

### 📁 File Upload API
- Upload movie posters, images, and news thumbnails  
- Files are stored in the Django media directory  
- Retrieve and display uploaded media on the frontend  

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | React, Tailwind CSS |
| Backend | Django, Django REST Framework |
| Authentication | JWT (SimpleJWT) |
| Database | PostgreSQL / SQLite |
| API Type | RESTful API |
| Deployment | (Optional) AWS / Render / Vercel |

---

## 🔑 Key API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/auth/signup/` | POST | Register a new user |
| `/api/auth/login/` | POST | Log in and receive JWT token |
| `/api/movies/` | GET | Get list of movies |
| `/api/movies/<id>/` | GET | Movie detail view |
| `/api/cart/` | GET, POST, DELETE | Manage shopping cart |
| `/api/tickets/` | POST | Book movie tickets |
| `/api/news/` | GET | List all news posts |
| `/api/news/<id>/comments/` | POST | Add a comment |

---

## 🧠 How It Works

1. Visitors can explore available movies and read movie-related news.  
2. To buy a movie or book a ticket, the user must log in or sign up.  
3. Authenticated users can:  
   - Add/remove movies from the shopping cart  
   - Confirm purchases  
   - Book cinema seats  
   - Comment on news articles  
4. The admin panel manages movies, bookings, users, and blog content.  

---

## 🛠️ Features Implemented

✅ **User Authentication System** — Login, signup, logout, JWT  
✅ **File Upload API** — Upload and display images for movies & posts  
✅ **RESTful Blog API** — Movie news, posts, and user comments  
✅ **E-commerce Backend** — Shopping cart, checkout, product management  
✅ **Event Tickets Booking System** — Create events, book seats, admin control  

---
