# Products API (Flask + SQLite)

A simple RESTful API built with Flask and SQLite for managing products.

---

## 🚀 Features
- Add product
- Get all products
- Delete product by ID
- Update product by ID
- Search product by name

---

## 🛠️ Tech Stack
- Python
- Flask
- SQLite

---

## 📌 API Endpoints

### Get all products
GET /products

### Add product
POST /products

### Delete product
DELETE /products/<id>

### Update product
PUT /products/<id>

### Search product
GET /products/search?name=product_name

---

## ▶️ How to run

```bash
pip install flask sqlite3
python app.py

## 👩‍💻 Author
Toqa - Backend Developer (Learning Phase)