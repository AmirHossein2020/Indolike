# 🗒️ Online Notebook

A simple **online notebook web app** built with **Django** and **Django REST Framework**, featuring user authentication, note management (CRUD), file & image upload, and URL shortening.  
The frontend is implemented using **HTML** and **CSS**, providing a clean and minimal user interface.

---

## 🚀 Main Features

### 🧑‍💻 User Authentication System
**Features:**
- User registration (Sign Up)
- User login (Sign In)
- User logout
- JWT (JSON Web Token) authentication for secured APIs

---

### 🗒️ Notes Management (CRUD)
**Features:**
- Create, read, update, and delete notes  
- Each note includes a **title**, **body text**, and optional **file or image attachments**  
- View all notes created by the logged-in user  
- Automatic **short URL generation** for each note

---

### 📎 File & Image Upload
**Features:**
- Upload files and images while creating or editing a note  
- Files are securely stored in the project’s media directory  
- Uploaded files can be viewed in the note detail page

---

### 🔗 URL Shortener
**Features:**
- Shorten any long URL via a simple API  
- Redirect users from a short link to the original URL  
- Integrated internally with the Notes app (each note has a short URL)

---

## 🧠 How It Works

1. A user must **sign up** or **log in** to access their notebook.  
2. After logging in, they are taken to the main page with three options:  
   - ✏️ Create a new note  
   - 📋 View list of notes  
   - 🚪 Logout  
3. When creating a note:
   - The user adds a title, body, and optionally uploads a file or image.  
4. On the note list page:
   - The user can **view**, **edit**, or **delete** any of their notes.  

> 🔍 Currently, search and filtering features are **not implemented**.

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django, Django REST Framework |
| Frontend | HTML, CSS |
| Authentication | JWT (SimpleJWT) |
| Database | SQLite |
| File Handling | Django File Storage |
| URL Shortener | Custom Django App |

---

## 🧩 Project Structure
