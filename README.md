# Products API — Flask REST API with JWT Authentication

A RESTful API built with Flask and SQLite for managing products with JWT authentication, protected routes, input validation, and clean backend architecture.

---

## 🚀 Features

- User registration & login
- JWT authentication
- Protected routes
- Add product
- Get all products
- Update product
- Delete product
- Search products
- Input validation
- Logging & error handling
- Environment variables support

---

## 🛠️ Tech Stack

- Python
- Flask
- SQLite
- JWT
- Gunicorn
- Render

---

## 🔐 Authentication

Protected routes require JWT token.

Example Header:

```http
Authorization: Bearer YOUR_TOKEN
```

---

## 📌 API Endpoints

### Register User

```http
POST /register
```

Request Body:

```json
{
  "username": "toqa",
  "password": "123456"
}
```

---

### Login User

```http
POST /login
```

Request Body:

```json
{
  "username": "toqa",
  "password": "123456"
}
```

Response Example:

```json
{
  "success": true,
  "token": "JWT_TOKEN"
}
```

---

### Get All Products

```http
GET /products
```

---

### Add Product

```http
POST /products
```

Protected Route ✅

Request Body:

```json
{
  "name": "milk"
}
```

---

### Update Product

```http
PUT /products/<id>
```

Protected Route ✅

Request Body:

```json
{
  "name": "Pasta"
}
```

---

### Delete Product

```http
DELETE /products/<id>
```

Protected Route ✅

---

### Search Product

```http
GET /products/search?name=product_name
```

---

## 🌐 Live Demo

```http
https://products-api-flask.onrender.com/products
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Ttuqqa/products-api-flask.git
```

### 2️⃣ Navigate to the project folder

```bash
cd products-api-flask
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` file

```env
SECRET_KEY=your_secret_key
```

### 5️⃣ Run the server

```bash
python app.py
```

---

## 👩‍💻 Author

Toqa — Backend Developer (Python & Flask)

---